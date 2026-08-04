---
title: Rust 概览
tags: [Rust, 编程语言, 内存安全, 系统编程, 所有权, 并发, 零成本抽象]
created: 2026-08-04
updated: 2026-08-04
related:
  - "[[Go 概览]]"
  - "[[Rust 实战代码库]]"
  - "[[编程语言 MOC]]"
---

# Rust 概览

> [!abstract] 30 秒速览
> Rust 是 Mozilla 发起的系统级语言，核心卖点是**内存安全无需垃圾回收（GC）**——靠编译期的**所有权（Ownership）/借用（Borrowing）/生命周期（Lifetime）** 三件套在编译时消除数据竞争与悬垂指针。2026 年稳定基准是 **Edition 2024（Rust 1.85+）**，`async fn in traits`（AFIT）已稳定且零成本。被 CISA/白宫点名推荐为内存安全语言；Google（Android/ChromeOS/Fuchsia）、微软（Windows 内核）均有生产采用。适合写性能敏感、安全关键的系统代码。

---

## 1. 为什么是 Rust（三大支柱）

| 支柱 | 含义 | 对你的价值 |
|---|---|---|
| **内存安全无 GC** | 编译期所有权检查，运行时无垃圾回收开销 | 无 GC 停顿，确定性延迟——适合系统/实时 |
| **零成本抽象** | 高层写法（trait、泛型、async）编译后与手写底层等价 | 安全不牺牲性能 |
| **无畏并发（Fearless Concurrency）** | 编译器保证无数据竞争（Send/Sync） | 多核时代写并发更安全 |

> 与 C/C++ 的本质区别：安全是**默认且由编译器强制**的，`unsafe` 是显式、可控、可审计的局部逃逸舱口，没有"全局不安全模式"。

## 2. 核心：所有权三件套（最难也最关键）

```rust
fn main() {
    let s1 = String::from("hello");
    let s2 = s1;            // 移动（move）：所有权转移，s1 此后失效
    // println!("{}", s1); // ❌ 编译错误：value borrowed after move
    let s3 = s2.clone();    // 显式深拷贝
    println!("{} {}", s2, s3);
}
```

- **所有权**：每个值有唯一所有者，所有者离开作用域自动释放（RAII，无 GC）。
- **借用**：`&T`（不可变引用）/ `&mut T`（可变引用）；**同一时刻要么多个不可变借用，要么一个可变借用**——编译期杜绝数据竞争。
- **生命周期 `'a`**：标注引用有效范围，编译器据此保证不出现悬垂引用（多数情况可自动推断，无需手写）。

> 心智模型：Rust 把"谁负责清理内存、谁能在何时访问"从运行时提前到编译期。这是它学习曲线陡的根源，也是安全的来源。

## 3. 类型系统与表达力

- **struct / enum（代数数据类型）**：`enum` 可携带数据，配合 `match` 做 exhaustive 模式匹配（比 C 的 enum 强得多）。
- **trait**：类似接口但更强（默认方法、关联类型、泛型约束）。
- **泛型 + 关联类型**：零成本多态。
- **模式匹配**：`match`、`if let`、`let-else`、`let-chains`（1.88+）大幅减少模板代码。
- **Option<T> / Result<T, E>**：用类型系统消灭"空指针"和"未处理错误"——`None`/`Err` 必须显式处理。

```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 { Err("divide by zero".into()) }
    else { Ok(a / b) }
}
// 调用方必须处理 Ok/Err：
let r = divide(10.0, 2.0)?;  // ? 把 Err 向上传播
```

## 4. 错误处理

- `Result<T, E>` + `?` 操作符：错误向上传播，强制处理。
- `thiserror`（2.0）：定义库的错误类型。
- `anyhow`：应用层便捷错误处理。
- 2026 新增：`core::error::Error` 支持 `no_std`（嵌入式也能用）。

## 5. 并发与异步

### 5.1 标准库线程
`std::thread`、`mpsc` 通道、`Arc<Mutex<T>>` 共享可变状态（Send/Sync 自动保证安全）。

### 5.2 Async（Edition 2024 是分水岭）
- **`async fn in traits`（AFIT，1.75 稳定，Edition 2024 完善）**：trait 里写原生异步方法，**零堆分配、静态分发**，告别 `async-trait` crate 的 `Box::pin`  workaround。
- **async 闭包**（1.85）：`async || { ... }`。
- **运行时**：Tokio 主导（I/O/定时器/任务调度），smol 轻量，Embassy 面向嵌入式 `no_std`。
- 生态主流（tower/hyper/axum/sqlx）已迁原生 AFIT。

```rust
trait DataStore {
    async fn fetch(&self, key: &str) -> Result<Vec<u8>, Error>; // 原生异步 trait，无 Box
}
```

> 仍存的边缘：auto trait（Send/Sync）跨 async trait 传递较棘手；async trait 非对象安全（`dyn AsyncTrait` 受限）；async 迭代器（gen blocks）仍nightly。这些是 2026–2027 路线图的收尾项。

## 6. 工具与生态

- **cargo**：构建/测试/依赖/发布一体化。
- **crates.io**：注册表 2025 年破 **16 万 crate**，下载量年增。
- **rustup**：版本/工具链管理；**rustfmt / clippy**：格式化 +  lint。
- **Edition 机制**：用 edition 而非大版本断裂来演进语言（2021 → 2024），平滑升级。

## 7. 安全采用与行业态势（2026）

- **政策背书**：美国 CISA 与白宫国家网络总监办公室推荐内存安全语言，点名 Rust。
- **大厂生产采用**：Amazon（Firecracker/Bottlerocket/S3）、Google（**Android/ChromeOS/Fuchsia**）、Microsoft（**Windows 内核组件/Azure**）、Meta、Cloudflare（Pingora）。
- **与 C++ 共存**：`cxx` crate 提供零开销 Rust↔C++ FFI；Android、Chromium、Linux 内核都是 Rust + C++ 并存，新系统代码默认 Rust、旧 C++ 渐进加安全层。

## 8. 2026 特性时间线

| 版本/Edition | 关键能力 |
|---|---|
| Rust 1.75 | `async fn in traits`(AFIT)、RPITIT 稳定 |
| **Edition 2024（1.85）** | 生命周期自动捕获、async 闭包、改进作用域语义、resolver v3 |
| 1.88 | `let-chains`（`a && b && let Some(x) = ...`） |
| 近期 | async 迭代器/gen blocks（nightly）、pin 人体工学、pattern types 在路上 |

类型系统"实用层面已基本完整"：GATs、RPITIT、trait upcasting 均稳定；TAIT、`!`（never type）仍待下一代 trait solver。

## 9. Rust vs Go vs C++

| 维度 | Rust | Go | C++ |
|---|---|---|---|
| 内存安全 | 编译期默认 | GC 运行时 | 手动/工具（profiles/sanitizer） |
| 抽象成本 | 零成本 | 少量运行时 | 零成本但易错 |
| 并发 | 无畏并发（编译保证） | goroutine 简单 | 需自己小心 |
| 学习曲线 | 陡 | 平缓 | 极陡 |
| 生态成熟度 | 快速成长（16万+crate） | 云原生极强 | 最庞大 |

## 10. 与 Android / AOSP 的强关联

- **Rust 正大举进入 Android 平台代码**：Google 在 Android、ChromeOS、Fuchsia 大量采用 Rust；AOSP 逐步引入 Rust 以减少内存安全漏洞（这正是 Android 平台历史漏洞的主因）。
- 对 **OS/Android PM** 而言：理解 Rust = 理解**平台底层安全模型的演进方向**，在评估"哪些模块该用 Rust 重写/新增"、做安全合规决策时具备技术对话能力。
- 与你在做的**系统级意图框架 / 端侧 Agent 安全**主题高度呼应：内存安全语言是"执行安全"的底层基石（见 [[隔离执行]]、[[Agent Data Injection 数据注入攻击]]）。

## 11. 学习路径

1. 官方 *The Rust Book* + Rustlings 交互练习（所有权章节反复嚼）。
2. 读 [[Rust 实战代码库]] 抄所有权/并发/async 片段。
3. 小项目：CLI（clap）、文件处理、再用 Tokio 写个异步服务。
4. 进阶：trait 对象 vs 泛型、Pin/Unpin、FFI 用 `cxx`、嵌入式 `no_std`。

> [!note] 相关概念
> [[Go 概览]] ｜ [[Rust 实战代码库]] ｜ [[编程语言 MOC]] ｜ [[OS-PM-系统AI Runtime vs 应用引擎]] ｜ [[隔离执行]] ｜ [[Agent Data Injection 数据注入攻击]]

## 深化补充

**心智模型**：Rust 的"默认安全、unsafe 是局部可审计逃生舱"恰是你做系统级 Agent 安全该照搬的治理哲学——意图框架也该"默认拒绝、高危操作走显式确认 UI（[[Agent 身份与硬件级审批]]），不安全的能力暴露是局部、可审计的例外"而非全局开放。Rust 在 Android 的渗透（减少内存安全漏洞）和你推"执行安全"是同一底层逻辑（对照 [[隔离执行]]、[[Agent Data Injection 数据注入攻击]]）。
