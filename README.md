# CryptoWatch

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/hanxiao199001/CryptoWatch?style=for-the-badge&logo=github)](https://github.com/hanxiao199001/CryptoWatch/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hanxiao199001/CryptoWatch?style=for-the-badge&logo=github)](https://github.com/hanxiao199001/CryptoWatch/network)
[![GitHub Issues](https://img.shields.io/github/issues/hanxiao199001/CryptoWatch?style=for-the-badge&logo=github)](https://github.com/hanxiao199001/CryptoWatch/issues)
[![License](https://img.shields.io/badge/license-GPL--2.0-green.svg?style=for-the-badge)](LICENSE)

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-orange?style=for-the-badge)](https://github.com/langchain-ai/langgraph)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-API-purple?style=for-the-badge)](https://www.deepseek.com)

</div>

<div align="center">
<h3>🔍 基于 LangGraph 的加密货币市场多智能体舆情分析系统</h3>
<p>灵感来源于 <a href="https://github.com/666ghj/BettaFish">BettaFish</a>，专注于 Web3 和加密货币领域的实时舆情监控与分析</p>
</div>

---

## ✨ 核心特性

<table>
<tr>
<td width="50%">

### 🤖 多智能体协作
基于 LangGraph 的智能体编排架构，各智能体协同工作，提供全方位分析

</td>
<td width="50%">

### ⛓️ Web3 数据集成
支持 CoinGecko、Etherscan 等主流数据源，实时获取链上数据

</td>
</tr>
<tr>
<td width="50%">

### 📊 实时舆情分析
自动化情感分析与趋势预测，及时发现市场动向

</td>
<td width="50%">

### 🧠 AI 驱动
集成 DeepSeek、Kimi 等先进大语言模型，提供智能洞察

</td>
</tr>
</table>

## 🏗️ 系统架构
```
CryptoWatch/
├── 📊 analysis_coordinator.py   # 分析协调器 - 统筹各智能体工作
├── 📡 data_agents.py            # 数据采集智能体 - 多源数据获取
├── 💬 forum_agents.py           # 论坛分析智能体 - 社区情绪分析
├── 📝 report_agent.py           # 报告生成智能体 - 结构化输出
├── ⛓️  web3_data_agent.py        # Web3数据智能体 - 链上数据分析
├── 🚀 bettafish_mini.py         # 主程序入口
├── 📚 docs/                     # 项目文档
│   ├── ARCHITECTURE.md       # 架构设计文档
│   ├── USER_GUIDE.md         # 详细使用指南
│   ├── PROJECT_SUMMARY.md    # 项目总结报告
│   └── installation.md       # 安装配置指南
└── 📦 requirements.txt          # Python依赖清单
```

## 🚀 快速开始

### 📋 环境要求

| 要求 | 版本 |
|------|------|
| Python | 3.11+ |
| PostgreSQL | 15+ |
| 内存 | 2GB+ |

### ⚙️ 安装步骤
```bash
# 1️⃣ 克隆仓库
git clone https://github.com/hanxiao199001/CryptoWatch.git
cd CryptoWatch

# 2️⃣ 创建虚拟环境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows

# 3️⃣ 安装依赖
pip install -r requirements.txt

# 4️⃣ 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入必要的 API 密钥

# 5️⃣ 运行主程序
python bettafish_mini.py
```

## 📖 文档

| 文档 | 描述 |
|------|------|
| [📐 系统架构](docs/ARCHITECTURE.md) | 深入了解系统设计理念和架构 |
| [📚 用户指南](docs/USER_GUIDE.md) | 详细的功能使用说明 |
| [📊 项目总结](docs/PROJECT_SUMMARY.md) | 项目概述、规划与展望 |
| [🔧 安装指南](docs/installation.md) | 详细的环境配置步骤 |

## 🤖 智能体说明

### 📡 Data Agents (数据采集智能体)
负责从各种数据源采集加密货币相关信息，包括：
- 💰 实时价格数据
- 📈 交易量统计
- 🐦 社交媒体动态
- 📰 新闻资讯

### 💬 Forum Agents (论坛分析智能体)
深度分析加密货币社区讨论：
- 🔥 热点话题识别
- 😊 情感倾向分析
- 📊 社区活跃度
- 💡 观点汇总

### ⛓️ Web3 Data Agent (链上数据智能体)
获取和分析区块链数据：
- 💸 交易数据分析
- 📜 智能合约活动
- 🏦 DeFi 协议监控
- 🎨 NFT 市场动态

### 📝 Report Agent (报告生成智能体)
整合分析结果，生成专业报告：
- 📊 数据可视化
- 📈 趋势预测
- 💡 投资建议
- ⚠️ 风险提示

### 📊 Analysis Coordinator (分析协调器)
统筹智能体协同工作：
- 🔄 任务分配
- ⏱️ 流程控制
- 🔗 数据聚合
- ✅ 结果验证

## 🛠️ 技术栈

<p align="center">
<img src="https://img.shields.io/badge/LangGraph-FF6B6B?style=for-the-badge&logo=python&logoColor=white" alt="LangGraph"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white" alt="LangChain"/>
<img src="https://img.shields.io/badge/DeepSeek-6366F1?style=for-the-badge&logo=openai&logoColor=white" alt="DeepSeek"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

## 📊 使用示例
```python
from bettafish_mini import CryptoAnalyzer

# 初始化分析器
analyzer = CryptoAnalyzer()

# 分析特定加密货币
result = analyzer.analyze("Bitcoin")

# 查看分析结果
print(f"📊 情感得分: {result.sentiment_score}")
print(f"📈 趋势预测: {result.trend_prediction}")
print(f"💡 投资建议: {result.recommendation}")
```

## 🤝 参与贡献

我们欢迎所有形式的贡献！

1. 🍴 Fork 本仓库
2. 🌿 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 💾 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 📤 推送到分支 (`git push origin feature/AmazingFeature`)
5. 🔀 开启 Pull Request

详见 [贡献指南](CONTRIBUTING.md)

## 📝 开发路线图

- [x] ✅ 基础架构搭建
- [x] ✅ 多智能体系统实现
- [x] ✅ 数据采集模块
- [ ] 🚧 Web UI 界面
- [ ] 📱 实时预警系统
- [ ] 🐳 Docker 部署支持
- [ ] 🔌 RESTful API 服务
- [ ] 📊 可视化仪表板

## 💡 致谢

本项目灵感来源于 [BettaFish](https://github.com/666ghj/BettaFish)，感谢原作者 [@666ghj](https://github.com/666ghj) 的开源贡献！

## 📄 许可证

本项目采用 [GPL-2.0](LICENSE) 许可证。

## 📮 联系方式

<p align="center">
<a href="https://github.com/hanxiao199001"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="mailto:han272624836@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
</p>

---

<div align="center">

### ⭐ 如果这个项目对你有帮助，请给个 Star 支持一下！

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hanxiao199001/CryptoWatch&type=Date)](https://star-history.com/#hanxiao199001/CryptoWatch&Date)

**Made with ❤️ by [@hanxiao199001](https://github.com/hanxiao199001)**

</div>
