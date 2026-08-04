---
title: LangChain 菜鸟教程
source: https://www.runoob.com/langchain/langchain-tutorial.html
tags: [LangChain, AI Agent, LLM, 教程, 菜鸟教程]
created: 2026-08-04
---

# LangChain 菜鸟教程（菜鸟教程整理）

> [!abstract] 摘要
> 本文整理自菜鸟教程《LangChain 教程》 landing 页。LangChain 是一套用于构建 AI 智能体（AI Agent）和大语言模型（LLM）应用的开发框架，由 Harrison Chase 于 2022 年 10 月推出，目标是简化 LLM 应用开发流程。它提供统一接口，连接大模型、Prompt、向量数据库、工具调用、记忆系统与 Agent 工作流。

---

## 一、LangChain 是什么

LangChain 可以帮助开发者快速构建基于 GPT、Claude、Gemini 等大模型的复杂 AI 应用。

- **推出时间**：2022 年 10 月，作者 Harrison Chase
- **核心目标**：简化大语言模型应用开发流程
- **统一接口可连接**：大模型、Prompt、向量数据库、工具调用、记忆系统、Agent 工作流
- **应用现状**：已成为最热门的 LLM 应用开发框架之一，广泛用于智能聊天机器人、RAG 知识库、文档分析、代码生成、AI 自动化等场景

## 二、谁适合阅读本教程

- 有 Python 基础，想学习 AI 与大语言模型开发的新手
- 想开发 AI 聊天机器人、知识库、Agent 应用的开发者
- 对 GPT、Claude、RAG、向量数据库感兴趣的学习者
- 希望使用 LangChain 快速构建 AI 项目的工程师
- 想从传统开发转向 AI 应用开发的程序员

## 三、学习前需要了解

- **Python 基础**：变量、函数、类、模块导入、异常处理
- **HTTP 与 API 基础**：GET/POST 请求、JSON 数据格式
- **Prompt 基础**：了解什么是 Prompt 与大语言模型
- **基础数据库知识**：了解 SQLite / MySQL 基础操作
- **命令行与 pip**：了解基本命令行操作与 pip 包管理

## 四、LangChain 可以做什么

- AI 聊天机器人（ChatBot）
- RAG 企业知识库
- PDF 文档问答系统
- AI Agent 自动任务执行
- 代码生成与代码分析
- 多轮对话与上下文记忆
- 联网搜索与工具调用
- 工作流自动化系统

## 五、第一个 LangChain 程序

以下代码使用 LangChain 调用 OpenAI 模型，并输出 AI 生成内容：

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# 初始化模型
llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# Prompt 模板
prompt = ChatPromptTemplate.from_template(
    "请解释：{topic}"
)

# 创建 Chain
chain = prompt | llm

# 调用
result = chain.invoke({
    "topic": "什么是 Transformer"
})

print(result.content)
```

运行后，大模型会自动生成关于 Transformer 的解释内容。

## 六、LangChain 核心组件

| 组件 | 作用 |
|---|---|
| **LLM** | 连接 OpenAI、Claude、Gemini 等大模型 |
| **PromptTemplate** | 管理 Prompt 模板 |
| **Chains** | 构建多步骤 AI 工作流 |
| **Memory** | 实现多轮对话记忆 |
| **Tools** | 调用搜索、数据库、API 等工具 |
| **Agents** | 让 AI 自动决策与执行任务 |
| **Vector Store** | 连接向量数据库实现 RAG |

## 七、参考文档

- LangChain 官网：https://www.langchain.com/
- LangChain Python 文档：https://python.langchain.com/
- LangChain JavaScript 文档：https://js.langchain.com/
- LangChain GitHub：https://github.com/langchain-ai/langchain

---

> [!note] 延伸阅读
> - 本库更系统的整理见 [[LangChain 概览]]（含架构分层、LCEL、检索器、记忆、生态、2026 动态与可运行代码库 [[LangChain 实战代码库]]）。
> - 有状态编排层见 [[LangGraph 概览]]；两者对比见 [[LangChain vs LangGraph 对比]]。
> - 检索增强生成（RAG）全流程见 [[RAG 检索增强生成]]。
> - Agent 框架的注入风险与 [[Agent Data Injection 数据注入攻击]] 主题相关——RAG 的"检索内容当作可信上下文"本身也是 ADI 的潜在靶面。

## 深化补充

**心智模型**：菜鸟教程那句"统一接口连模型/工具/记忆"，正是 LangChain 全部价值的浓缩；抓住这层，再去看系统意图框架"OS 级 Tool Calling"就不会觉得是两个东西（见 [[应用层 Agent 框架 vs 系统级意图框架 对照]]）——只是 `@tool` 换成了 `@AppIntent`，契约之外多出系统授权。

**待解问题**
- [ ] 新手从"调 OpenAI"入门到理解"App Intent 是 OS 级 @tool"，中间缺哪一层概念桥？我将来带人时怎么补？
