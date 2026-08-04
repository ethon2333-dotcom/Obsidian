---
title: Go 实战代码库
tags: [Go, 代码, 实战, 并发, channel, 泛型, cookbook]
created: 2026-08-04
updated: 2026-08-04
related:
  - "[[Go 概览]]"
  - "[[Rust 实战代码库]]"
---

# Go 实战代码库

> [!abstract] 一句话
> 可直接抄的 Go 代码片段：基础语法、接口、错误处理、并发（goroutine/channel/select/context）、HTTP、JSON、泛型、测试。配合 [[Go 概览]] 阅读。

---

## 1. Hello + 基础

```go
package main

import "fmt"

func main() {
    name := "Ethon"          // 短声明 + 类型推断
    age := 30
    fmt.Printf("%s is %d\n", name, age)
}
```

## 2. 结构体 / 方法 / 接口（隐式实现）

```go
type Speaker interface {
    Speak() string
}

type Dog struct{ Name string }
func (d Dog) Speak() string { return d.Name + " says woof" }

type Cat struct{ Name string }
func (c Cat) Speak() string { return c.Name + " says meow" }

// 任意实现了 Speak() 的类型都自动满足 Speaker，无需声明 implements
func announce(s Speaker) { fmt.Println(s.Speak()) }

func main() {
    announce(Dog{"Rex"})
    announce(Cat{"Mimi"})
}
```

## 3. 错误处理范式

```go
import "errors"

func readConfig(path string) (string, error) {
    if path == "" {
        return "", errors.New("path required")
    }
    // ... 读文件，可能返回 err
    return "ok", nil
}

func main() {
    if v, err := readConfig(""); err != nil {
        fmt.Println("error:", err)
        return
    } else {
        fmt.Println(v)
    }
}
```

`defer` + `recover` 捕获 panic（类似兜底异常，慎用）：

```go
defer func() {
    if r := recover(); r != nil {
        fmt.Println("recovered:", r)
    }
}()
```

## 4. Goroutine + Channel（并发基础）

```go
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {          // 从通道取任务，通道关闭时退出
        results <- j * 2
    }
}

func main() {
    jobs := make(chan int, 10)
    results := make(chan int, 10)

    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results) // 启动 3 个 worker goroutine
    }
    for j := 1; j <= 5; j++ { jobs <- j }
    close(jobs)
    for i := 1; i <= 5; i++ { fmt.Println(<-results) }
}
```

## 5. select + 超时

```go
select {
case res := <-results:
    fmt.Println("got", res)
case <-time.After(2 * time.Second):
    fmt.Println("timeout")
}
```

## 6. sync.WaitGroup 等待一组 goroutine

```go
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Println("worker", id)
    }(i)
}
wg.Wait() // 阻塞直到全部 Done
```

## 7. context 取消传播（生产必用）

```go
ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
defer cancel()

go func() {
    select {
    case <-time.After(5 * time.Second):
        fmt.Println("slow work done")
    case <-ctx.Done():              // 超时/被取消时收到信号
        fmt.Println("canceled:", ctx.Err())
    }
}()
time.Sleep(4 * time.Second)
```

## 8. HTTP 服务（标准库）

```go
func main() {
    http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "hello %s", r.URL.Query().Get("name"))
    })
    http.ListenAndServe(":8080", nil)
}
```

## 9. JSON 序列化

```go
type User struct {
    Name  string `json:"name"`
    Email string `json:"email,omitempty"` // omitempty：空值不输出
}

u := User{Name: "Ethon"}
b, _ := json.Marshal(u)            // -> {"name":"Ethon"}
var out User
json.Unmarshal(b, &out)
```

## 10. 泛型（1.18+，1.24 支持泛型类型别名）

```go
func Max[T int | float64 | string](a, b T) T {
    if a > b { return a }
    return b
}

// 泛型类型别名（1.24+）
type Set[T comparable] = map[T]bool
```

## 11. 测试

```go
// main_test.go
func TestDivide(t *testing.T) {
    if _, err := divide(1, 0); err == nil {
        t.Fatal("expected error for divide by zero")
    }
}
// 运行：go test ./...  竞态检测：go test -race ./...
```

## 12. 并发模式提示

- **Pipeline**：用多个 channel 串联阶段，每阶段 goroutine 消费/生产。
- **Fan-out**：多个 worker 消费同一 channel 并行处理；**Fan-in**：多个 channel 合并到一个。
- **Worker Pool**：固定数量 worker + 任务 channel（见第 4 节），控制并发度。

> [!note] 相关概念
> [[Go 概览]] ｜ [[Rust 实战代码库]] ｜ [[编程语言 MOC]] ｜ [[OS-PM-系统AI Runtime vs 应用引擎]]

## 深化补充

**关联指针**：第 4/5/7 节的 worker pool、`select`+超时、`context` 取消传播，正是系统级 Agent 把"一个用户意图拆成多步、任一步超时/取消要能干净退出"的工程原型——把 `context` 类比成 [[System Orchestrator 系统编排]] 下发给每个子意图的"取消令牌"即可。代码库里的 `context` 是理解"编排如何不拖垮整条链"的最小可运行样例。
