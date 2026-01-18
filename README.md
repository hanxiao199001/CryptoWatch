# CryptoWatch

[![GitHub Stars](https://img.shields.io/github/stars/hanxiao199001/CryptoWatch?style=flat-square)](https://github.com/hanxiao199001/CryptoWatch/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hanxiao199001/CryptoWatch?style=flat-square)](https://github.com/hanxiao199001/CryptoWatch/network)
[![GitHub Issues](https://img.shields.io/github/issues/hanxiao199001/CryptoWatch?style=flat-square)](https://github.com/hanxiao199001/CryptoWatch/issues)
[![License](https://img.shields.io/badge/license-GPL--2.0-green.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square)](https://www.python.org)

> 🔍 基于 LangGraph 的加密货币市场多智能体舆情分析系统
>
> 灵感来源于 [BettaFish](https://github.com/666ghj/BettaFish)，专注于 Web3 和加密货币领域的实时舆情监控与分析。

## ✨ 核心特性

- 🤖 **多智能体协作**: 基于 LangGraph 的智能体编排架构
- ⛓️ **Web3 数据集成**: 支持 CoinGecko、Etherscan 等主流数据源
- 📊 **实时舆情分析**: 自动化情感分析与趋势预测
- 🧠 **AI 驱动**: 集成 DeepSeek、Kimi 等先进大语言模型
- 🔄 **灵活扩展**: 模块化设计，易于定制和扩展

## 🏗️ 系统架构
```
CryptoWatch/
├── analysis_coordinator.py   # 分析协调器
├── data_agents.py            # 数据采集智能体
├── forum_agents.py           # 论坛分析智能体
├── report_agent.py           # 报告生成智能体
├── web3_data_agent.py        # Web3 数据智能体
├── bettafish_mini.py         # 主程序入口
├── docs/                     # 项目文档
│   ├── ARCHITECTURE.md       # 架构设计
│   ├── USER_GUIDE.md         # 使用指南
│   └── PROJECT_SUMMARY.md    # 项目总结
└── requirements.txt          # 依赖清单
```

## 🚀 快速开始

### 环境要求

- Python 3.11+
- PostgreSQL 15+
- 2GB+ RAM

### 安装步骤
```bash
# 1. 克隆仓库
git clone https://github.com/hanxiao199001/CryptoWatch.git
cd CryptoWatch

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入必要的 API 密钥

# 5. 运行主程序
python bettafish_mini.py
```

## 📖 文档

- [📐 系统架构](docs/ARCHITECTURE.md) - 了解系统设计理念
- [📚 用户指南](docs/USER_GUIDE.md) - 详细使用说明
- [📊 项目总结](docs/PROJECT_SUMMARY.md) - 项目概述与规划
- [🔧 安装指南](docs/installation.md) - 详细安装步骤

## 🤖 智能体说明

### Data Agents (数据采集)
负责从各种数据源采集加密货币相关信息，包括价格、交易量、社交媒体数据等。

### Forum Agents (论坛分析)
分析加密货币社区讨论，提取热点话题和情感倾向。

### Web3 Data Agent (链上数据)
获取和分析区块链上的交易数据、智能合约活动等。

### Report Agent (报告生成)
整合各智能体的分析结果，生成结构化的分析报告。

### Analysis Coordinator (协调器)
协调各个智能体的工作流程，确保系统高效运行。

## 🛠️ 技术栈

- **LangGraph**: 智能体工作流编排
- **LangChain**: LLM 应用开发框架
- **DeepSeek**: 推理与分析
- **Kimi**: 长文本处理
- **PostgreSQL**: 数据持久化
- **Python 3.11+**: 开发语言

## 📊 使用示例
```python
from bettafish_mini import CryptoAnalyzer

# 初始化分析器
analyzer = CryptoAnalyzer()

# 分析特定加密货币
result = analyzer.analyze("Bitcoin")
print(f"情感得分: {result.sentiment_score}")
print(f"趋势预测: {result.trend_prediction}")
```

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

详见 [贡献指南](CONTRIBUTING.md)

## 📝 开发计划

- [x] 基础架构搭建
- [x] 多智能体系统实现
- [ ] Web UI 界面
- [ ] 实时预警系统
- [ ] Docker 部署支持
- [ ] API 服务接口

## 💡 致谢

本项目灵感来源于 [BettaFish](https://github.com/666ghj/BettaFish)，感谢原作者的开源贡献。

## 📄 许可证

本项目采用 [GPL-2.0](LICENSE) 许可证。

## 📮 联系方式

- **作者**: hanxiao199001
- **Email**: han272624836@gmail.com
- **GitHub**: [@hanxiao199001](https://github.com/hanxiao199001)

---

⭐ 如果这个项目对你有帮助，请给个 Star 支持一下！

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hanxiao199001/CryptoWatch&type=Date)](https://star-history.com/#hanxiao199001/CryptoWatch&Date)
