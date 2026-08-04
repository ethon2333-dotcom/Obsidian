---
title: Rust 实战代码库
tags: [Rust, 代码, 实战, 所有权, 并发, async, tokio, cookbook]
created: 2026-08-04
updated: 2026-08-04
related:
  - "[[Rust 概览]]"
  - "[[Go 实战代码库]]"
---

# Rust 实战代码库

> [!abstract] 一句话
> 可直接抄的 Rust 代码片段：所有权、结构体/枚举、模式匹配、trait/泛型、错误处理、并发（线程/channel/Arc<Mutex>）、async/Tokio、cargo 工程。配合 [[Rust 概览]] 阅读。

---

## 1. Hello + 变量

```rust
fn main() {
    let name = "Ethon";      // 不可变绑定（默认）
    let mut age = 30;        // mut：可变
    age += 1;
    println!("{} is {}", name, age);
}
```

## 2. 所有权与借用

```rust
fn takes_ownership(s: String) { println!("{}", s); } // s 在此被丢弃
fn borrows(s: &String) { println!("{}", s); }        // 只读借用，不转移

fn main() {
    let s = String::from("hi");
    borrows(&s);              // 借出不转移，s 仍可用
    takes_ownership(s);       // 转移，s 此后失效
    // println!("{}", s);     // ❌ 编译错误
}
```

## 3. 结构体 + 方法 + 枚举 + match

```rust
#[derive(Debug)]
struct User { name: String, active: bool }

enum Msg { Quit, Move { x: i32, y: i32 }, Text(String) }

fn handle(m: Msg) {
    match m {
        Msg::Quit => println!("quit"),
        Msg::Move { x, y } => println!("move to {},{}", x, y),
        Msg::Text(t) => println!("text: {}", t),
    }
}
```

## 4. 错误处理（Result + ?）

```rust
use std::num::ParseIntError;

fn parse(s: &str) -> Result<i32, ParseIntError> {
    let n: i32 = s.parse()?;   // ? 把 Err 向上传播
    Ok(n * 2)
}

fn main() {
    match parse("42") {
        Ok(v) => println!("{}", v),
        Err(e) => println!("error: {}", e),
    }
}
```

## 5. trait + 泛型

```rust
trait Summary {
    fn summarize(&self) -> String;
}

struct Article { title: String }
impl Summary for Article {
    fn summarize(&self) -> String { format!("Article: {}", self.title) }
}

// 泛型约束：任何实现 Summary 的类型都可用
fn notify<T: Summary>(item: &T) { println!("{}", item.summarize()); }
```

## 6. 迭代器与闭包（零成本）

```rust
let v: Vec<i32> = (1..=10).filter(|x| x % 2 == 0).map(|x| x * x).collect();
// -> [4, 16, 36, 64, 100]
```

## 7. 并发：线程 + 通道 + Arc<Mutex>

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];
    for _ in 0..5 {
        let c = Arc::clone(&counter);
        handles.push(thread::spawn(move || {
            let mut num = c.lock().unwrap();
            *num += 1;
        }));
    }
    for h in handles { h.join().unwrap(); }
    println!("result: {}", *counter.lock().unwrap()); // -> 5
}
```

## 8. 异步：Tokio（Edition 2024 + AFIT）

`Cargo.toml`：
```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
```

```rust
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() {
    let h1 = tokio::spawn(async {
        sleep(Duration::from_millis(100)).await;
        "task1"
    });
    let h2 = tokio::spawn(async { "task2" });
    println!("{} {}", h1.await.unwrap(), h2.await.unwrap());
}
```

原生 async trait（零成本，无需 async-trait crate）：
```rust
trait Store {
    async fn get(&self, key: &str) -> Result<String, Error>;
}
```

## 9. cargo 工程骨架

```bash
cargo new myapp --bin     # 新建二进制项目
cargo build               # 构建
cargo run                 # 构建并运行
cargo test                # 跑测试
cargo clippy              # lint
cargo fmt                 # 格式化
```

`Cargo.toml` 片段：
```toml
[package]
name = "myapp"
version = "0.1.0"
edition = "2024"          # 用最新 edition

[dependencies]
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

## 10. 序列化（serde）

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct User { name: String, age: u8 }

let json = serde_json::to_string(&User { name: "Ethon".into(), age: 30 }).unwrap();
let u: User = serde_json::from_str(&json).unwrap();
```

## 11. 与 C++ 互操作（cxx，系统级常用）

```rust
#[cxx::bridge]
mod ffi {
    unsafe extern "C++" {
        include!("mylib/include/engine.h");
        type Engine;
        fn create_engine() -> UniquePtr<Engine>;
        fn process(self: &Engine, input: &[u8]) -> Vec<u8>;
    }
}
```

> [!note] 相关概念
> [[Rust 概览]] ｜ [[Go 实战代码库]] ｜ [[编程语言 MOC]] ｜ [[OS-PM-系统AI Runtime vs 应用引擎]] ｜ [[隔离执行]]

## 深化补充

**关联指针**：第 11 节的 `cxx` FFI 是理解"系统级 Agent 怎么在存量 C/C++ 平台代码上安全地加一层新能力"的钥匙——和 Android/AOSP 里"旧 C++ 渐进加 Rust 安全层"是同一思路。当你评估"某个端侧推理模块要不要用 Rust 重写来堵内存安全漏洞"时，这段互操作代码就是答案的边界：新逻辑用 Rust，旧引擎用 `cxx` 接进来，而非推倒重来。
