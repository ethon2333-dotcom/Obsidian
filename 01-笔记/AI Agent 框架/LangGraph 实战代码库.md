---
title: LangGraph 实战代码库
tags: [LangGraph, 代码, 实战, 状态机, 人工介入, 多智能体, 时间旅行, cookbook]
created: 2026-08-04
updated: 2026-08-04
related:
  - "[[LangGraph 概览]]"
  - "[[LangChain 实战代码库]]"
---

# LangGraph 实战代码库

> [!abstract] 一句话
> 可直接抄的 LangGraph 代码片段合集，覆盖状态机、ReAct、人工介入、时间旅行、条件边、多智能体、流式。配合 [[LangGraph 概览]] 的概念阅读。

---

## 1. 最小有状态图

```python
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

def node_a(state: AgentState):
    return {"messages": [HumanMessage(content="来自 A")]}

def node_b(state: AgentState):
    return {"messages": [HumanMessage(content="来自 B")]}

builder = StateGraph(AgentState)
builder.add_node("a", node_a)
builder.add_node("b", node_b)
builder.set_entry_point("a")
builder.add_edge("a", "b")
builder.add_edge("b", END)

app = builder.compile()
print(app.invoke({"messages": []})["messages"])
```

## 2. ReAct 工具调用 Agent（从零）

```python
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_anthropic import ChatAnthropic

def call_model(state):
    return {"messages": [llm.invoke(state["messages"])]}

def call_tool(state):
    last = state["messages"][-1]
    tool_msgs = []
    for tc in last.tool_calls:
        result = tools_by_name[tc["name"]].invoke(tc["args"])
        tool_msgs.append(ToolMessage(content=str(result), tool_call_id=tc["id"]))
    return {"messages": tool_msgs}

def should_continue(state) -> str:
    if state["messages"][-1].tool_calls:
        return "call_tool"
    return END

builder = StateGraph(AgentState)
builder.add_node("call_model", call_model)
builder.add_node("call_tool", call_tool)
builder.set_entry_point("call_model")
builder.add_conditional_edges("call_model", should_continue)
builder.add_edge("call_tool", "call_model")
app = builder.compile()
```

> 想省事可用预置 `create_react_agent(model, tools)`，但手写版便于理解四原语。

## 3. 持久化（Checkpointer）

```python
from langgraph.checkpoint.sqlite import SqliteSaver

memory = SqliteSaver.from_conn_string("agent_state.db")
app = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "session_001"}}
app.invoke({"messages": [HumanMessage("研究 2026 Agent 趋势")]}, config)
# 后续同一 thread_id 调用会延续全部状态
```

## 4. 人工介入（interrupt）

```python
app = builder.compile(
    checkpointer=memory,
    interrupt_before=["human_review"],   # 在 human_review 前暂停
)

app.invoke(inputs, config)
# 人类在 human_review 前介入审阅……
app.invoke(Command(resume="approved"), config)   # 恢复执行
```

## 5. 时间旅行 / 状态编辑

```python
state = app.get_state(config)            # 当前状态 + 下一步 + 待恢复点
print(state.values, state.next)

# 直接改写状态（纠错 / 注入人工决定）
app.update_state(config, {"messages": [HumanMessage("改用中文回答")]})
# 从某历史 checkpoint 重放
app.invoke(None, config)  # 重新执行到当前 next
```

## 6. 条件边 + Command（路由时同时更新状态）

```python
from langgraph.graph import Command

def router(state) -> Command:
    if state["risk_score"] > 0.8:
        return Command(goto="human_review", update={"flagged": True})
    if state["loop_count"] >= 5:
        return Command(goto=END)
    return Command(goto="analyst")
```

## 7. 多智能体：Supervisor 模式

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

def supervisor(state):
    # LLM 决定下一个干活的 worker
    decision = llm.invoke([system_prompt] + state["messages"]).content
    return {"next": decision}  # "worker_a" / "worker_b" / "FINISH"

builder = StateGraph(AgentState)
builder.add_node("supervisor", supervisor)
builder.add_node("worker_a", worker_a_node)
builder.add_node("worker_b", worker_b_node)
builder.add_conditional_edges("supervisor", lambda s: s["next"],
                              {"worker_a": "worker_a", "worker_b": "worker_b", "FINISH": END})
builder.add_edge("worker_a", "supervisor")
builder.add_edge("worker_b", "supervisor")
builder.set_entry_point("supervisor")
```

## 8. 多智能体：Collaborative（Swarm 对等共享消息）

```python
# 多个 Agent 共享同一 messages 通道，自主交接
class SwarmState(TypedDict):
    messages: Annotated[list, add_messages]
    active_agent: str

# 每个 agent 节点返回 Command(goto=下一个 agent 或 END)
# 适合无明确上下级、需要协商的协作场景
```

## 9. 流式输出模式

```python
# updates：仅增量（最常用）
for chunk in app.stream(inputs, config, stream_mode="updates"):
    print(chunk)

# messages：逐 token
for chunk in app.stream(inputs, config, stream_mode="messages"):
    print(chunk[0].content, end="", flush=True)

# values：每步完整状态快照
for chunk in app.stream(inputs, config, stream_mode="values"):
    print(chunk["messages"][-1])
```

## 10. 子图（嵌套编排）

```python
sub_builder = StateGraph(SubState)
sub_builder.add_node(...)
sub_graph = sub_builder.compile()

main = StateGraph(MainState)
main.add_node("subtask", sub_graph)   # 把一张图当节点用
main.add_edge("subtask", "next")
```

## 11. 生产清单

- State schema 保持干净强类型；长任务必用持久 Checkpointer（生产用 PostgresSaver）。
- 高风险动作前加 `interrupt_before` 做审批闸门（呼应 [[确认机制]]）。
- 用 LangSmith 监控节点级 trace；对 Agent 工具调用强制沙箱隔离（呼应 [[隔离执行]] 与 [[Agent Data Injection 数据注入攻击]]）。
- 关键决策点可 `update_state` 注入人工决定，支持审计与回滚。

> [!note] 相关概念
> [[LangGraph 概览]] ｜ [[LangChain 实战代码库]] ｜ [[LangChain vs LangGraph 对比]] ｜ [[确认机制]] ｜ [[隔离执行]] ｜ [[Agent Data Injection 数据注入攻击]]

## 深化补充

**心智模型**：片段 6 的 `Command(goto=..., update=...)` 条件路由，就是"意图参数决定下一步走向"的编程原型；系统层 ArkAF 的图推理引擎干的也是这件事，只是每跳前多了一次权限闸门判定。

**待解问题**
- [ ] LangGraph 的 State schema 强类型约束，对系统意图 Schema 设计有什么可借鉴的"不可漏字段"思路？
