---
title: LangChain 实战代码库
tags: [LangChain, 代码, 实战, LCEL, RAG, 工具调用, LangServe, cookbook]
created: 2026-08-04
updated: 2026-08-04
related:
  - "[[LangChain 概览]]"
  - "[[LangGraph 实战代码库]]"
---

# LangChain 实战代码库

> [!abstract] 一句话
> 可直接抄的 LangChain 代码片段合集，覆盖 LCEL、RAG、结构化输出、记忆、工具调用、LangServe、流式与兜底。配合 [[LangChain 概览]] 的概念阅读。

---

## 1. 最小 LCEL 链

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("把这句话翻译成英文：{text}")
llm = ChatAnthropic(model="claude-sonnet-4-6")
chain = prompt | llm | StrOutputParser()

print(chain.invoke({"text": "今天天气真好"}))
```

## 2. RAG 端到端（Chroma 向量库）

```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1) 载入 + 切分
docs = TextLoader("policy.txt", encoding="utf-8").load()
splits = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

# 2) 向量化入库
vectorstore = Chroma.from_documents(splits, OpenAIEmbeddings())

# 3) 检索 + 生成
retriever = vectorstore.as_retriever()
prompt = ChatPromptTemplate.from_template(
    "基于上下文回答：{context}\n\n问题：{question}"
)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt | ChatAnthropic(model="claude-sonnet-4-6") | StrOutputParser()
)

print(rag_chain.invoke("退款政策是什么？"))
```

## 3. 结构化输出（Pydantic）

```python
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_anthropic import ChatAnthropic

class Person(BaseModel):
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")

parser = PydanticOutputParser(pydantic_object=Person)
prompt = ChatPromptTemplate.from_messages([
    ("system", "提取人物信息：\n{format_instructions}"),
    ("human", "{text}"),
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | ChatAnthropic(model="claude-sonnet-4-6") | parser
print(chain.invoke({"text": "张三今年 30 岁"}))
# -> Person(name='张三', age=30)
```

> 现代模型也支持 `llm.with_structured_output(Person)` 原生结构化，更稳。

## 4. 多查询检索（MultiQueryRetriever）

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
)
# LLM 把原问题扩写成多角度问题，分别检索后合并，缓解单一问法漏召回
```

## 5. 对话记忆（Summary Buffer）

```python
from langchain.memory import ConversationSummaryBufferMemory
from langchain_anthropic import ChatAnthropic

memory = ConversationSummaryBufferMemory(
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    max_token_limit=1000,
    return_messages=True,
)
memory.save_context({"input": "我叫 Ethon"}, {"output": "你好 Ethon"})
# 长对话自动摘要，省钱且保留关键信息
```

## 6. 工具调用 Agent（@tool）

```python
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

@tool
def get_weather(city: str) -> str:
    """查询某城市天气。"""
    return f"{city} 今天晴，25°C"

tools = [get_weather]
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个助手，必要时调用工具。"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
agent = create_tool_calling_agent(ChatAnthropic(model="claude-sonnet-4-6"), tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print(executor.invoke({"input": "北京天气怎么样？"}))
```

> ⚠️ `AgentExecutor` 是**无状态线性循环**，复杂场景请迁 [[LangGraph 实战代码库]] 的图。

## 7. 并行 / 兜底 / 重试

```python
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

# 并行：同时跑两个分支
parallel = RunnableParallel({
    "summary": prompt_a | ChatAnthropic(...),
    "translate": prompt_b | ChatOpenAI(...),
})

# 兜底：主模型挂了切备用
chain = (prompt | ChatAnthropic(...)).with_fallbacks([prompt | ChatOpenAI(...)])
# 重试
chain = chain.with_retry(stop_after_attempt=3)
```

## 8. 流式与批处理

```python
# 流式（打字机）
for chunk in chain.stream({"text": "讲个笑话"}):
    print(chunk, end="", flush=True)

# 批处理（并发多个输入）
results = chain.batch([{"text": "A"}, {"text": "B"}, {"text": "C"}])
```

## 9. 用 LangServe 发布成 API

```python
# serve.py
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="My RAG API")
add_routes(app, rag_chain, path="/rag")
# 运行：langserve dev serve.py  -> 自带 Playground + OpenAPI
```

## 10. 生产小贴士

- 用 `RunnableConfig` 注入 `metadata={"user_id": ..., "tags": [...]}` 便于 LangSmith 计费与审计。
- 长文本切分优先 `RecursiveCharacterTextSplitter`；中文可配合按句/段切分。
- 检索后考虑 `ContextualCompressionRetriever` 压缩无关内容省 token。
- 敏感工具调用前务必加确认/沙箱（呼应 [[确认机制]] 与 [[Agent Data Injection 数据注入攻击]]）。

> [!note] 相关概念
> [[LangChain 概览]] ｜ [[LangGraph 实战代码库]] ｜ [[LangChain vs LangGraph 对比]] ｜ [[确认机制]] ｜ [[隔离执行]]

## 深化补充

**心智模型**：片段 7 的 `with_fallbacks` / `with_retry` 是应用层对"不可控运行时"的兜底写法，对应你在 [[OS-PM-AI Runtime动态调度与降级策略]] 里要做的全局降级——区别是应用层自己堆、系统层由 Runtime 统一仲裁。

**待解问题**
- [ ] 应用层用 `context` 持有取消令牌，端侧多 App 编排里这个"取消权"该由 Orchestrator 还是由触发 App 持有？
