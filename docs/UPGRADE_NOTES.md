# LangGraph 1.x 迁移要点

> 现状:`requirements.txt` 钉在 `langgraph>=0.0.20`(2024 年初的远古版本),
> 且当前代码实际上**没有调用任何 LangGraph API**——编排逻辑是 `analysis_coordinator.py`
> 里的手写协调器。因此"迁移"首先是一个架构决策,而不只是改 import。

## 0. 先做决策

两条路二选一:

- **A. 真正接入 LangGraph 1.x**(推荐,如果目标是学习/展示 LangGraph):
  用 `StateGraph` 重写 `analysis_coordinator.py` 的编排逻辑。
- **B. 移除 langgraph 依赖**:代码本来就没用到,直接从 requirements 删掉
  `langgraph`/`langchain`,项目立刻"诚实"且可安装。工作量最小。

以下按路线 A 展开。

## 1. 环境与依赖

- Python 升级到 **3.10+**(LangChain/LangGraph 1.x 要求)。
- `langgraph>=1.0`,`langchain>=1.0`;checkpointer 拆分为独立包:
  `langgraph-checkpoint-sqlite` / `langgraph-checkpoint-postgres`(按需)。
- `requirements-dev.txt` 中 black/flake8 可考虑换成 ruff,一并现代化。

## 2. 0.0.x → 1.x 的主要断裂点

| 0.0.x 时代 | 1.x 现状 |
|---|---|
| `MessageGraph` | 已移除,统一用 `StateGraph` + messages state |
| dict 随意当 state | state 必须是 TypedDict / Pydantic 模型 |
| `config_schema` | 改为 `context_schema`,运行时用 `Runtime` 注入 |
| `langgraph.prebuilt.create_react_agent` | 1.x 建议用 `langchain.agents.create_agent` |
| `langgraph.checkpoint.SqliteSaver` 内置 | 移到 `langgraph-checkpoint-sqlite` 独立包 |
| 手动断点做人工介入 | `interrupt()` + `Command(resume=...)` 一等公民 |
| `stream()` 返回结构旧格式 | `stream_mode="values"/"updates"/"messages"` 显式指定 |

## 3. 本项目的具体改造清单

1. **定义状态**:把协调器里传来传去的 dict 收敛成一个 `TypedDict`
   (如 `AnalysisState`: query / news / sentiment / onchain / forum_views / report)。
2. **节点化各 Agent**:`data_agents.py`、`web3_data_agent.py`、`forum_agents.py`、
   `report_agent.py` 各包装成节点函数 `(state) -> dict`。
3. **建图**:数据采集节点可并行(fan-out/fan-in),之后进论坛辩论节点,最后报告节点。
4. **LLM 调用**:直接用 openai SDK 的部分可保留,或换 `init_chat_model` 统一接口。
5. **持久化(可选)**:接 `langgraph-checkpoint-sqlite` 支持断点续跑。
6. **测试**:`tests/` 里对 mock 数据的单测基本可保留;新增对图编排的集成测试。

## 4. 数据源未实装项(与迁移无关但需一并处理)

- 未配置 `TAVILY_API_KEY` 时新闻数据返回内置模拟数据(`data_agents.py`);
- 情绪分析为模拟结果;`report_agent.py` 演示入口用模拟数据。
- 上线前需实装真实数据源并在 README 标注哪些是真数据、哪些是演示。
