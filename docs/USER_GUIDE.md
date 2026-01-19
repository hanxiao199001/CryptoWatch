# 📖 CryptoWatch - 用户手册

欢迎使用CryptoWatch! 本手册将帮助你快速上手这个强大的Multi-Agent舆情分析系统。

---

## 📋 目录

- [快速开始](#快速开始)
- [基础使用](#基础使用)
- [高级功能](#高级功能)
- [常见问题](#常见问题)
- [最佳实践](#最佳实践)

---

## 🚀 快速开始

### 第一步: 环境准备

1. **安装Python**
```bash
   # 检查Python版本
   python --version  # 需要 3.9+
```

2. **创建虚拟环境**
```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # Windows: venv\Scripts\activate
```

3. **安装依赖**
```bash
   pip install -r requirements.txt
```

### 第二步: 配置API密钥

1. **复制环境变量模板**
```bash
   cp .env.example .env
```

2. **编辑`.env`文件**
```bash
   # 必需配置
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   
   # 可选配置
   TAVILY_API_KEY=your_tavily_api_key_here
```

3. **获取API密钥**
   - DeepSeek: https://www.deepseek.com/
   - Tavily: https://www.tavily.com/

### 第三步: 运行第一个分析
```bash
python cryptowatch.py
```

🎉 看到完整的分析流程就说明成功了!

---

## 💻 基础使用

### 1. 完整分析

分析单个加密货币项目并生成报告:
```python
from cryptowatch import CryptoWatch

# 创建系统
betta = CryptoWatch()

# 分析Ethereum
result = betta.analyze(
    topic="Ethereum",
    coin_id="ethereum",
    save_report=True
)
```

**输出**:
- ✅ 实时市场数据
- ✅ 新闻资讯
- ✅ 社交媒体情绪
- ✅ AI专家分析
- ✅ Markdown报告文件

**报告位置**: `reports/analysis_YYYYMMDD_HHMMSS.md`

### 2. 快速市场检查

只获取价格数据,不生成完整报告:
```python
# 快速查看Bitcoin
betta.quick_market_check("bitcoin")
```

**输出示例**:
```
📊 市场快照:
======================================================================
💰 当前价格: $95,127.00
📈 24h变化: 0.06%
💎 市值: $1,900,197,964,905
📊 交易量: $19,325,521,228
======================================================================
```

### 3. 项目对比

对比多个加密货币:
```python
# 对比BTC, ETH, SOL
results = betta.compare_projects([
    ("Bitcoin", "bitcoin"),
    ("Ethereum", "ethereum"),
    ("Solana", "solana")
])
```

**输出示例**:
```
项目              价格        24h变化            市值
----------------------------------------------------------------------
Bitcoin      $95,127.00        0.06%  $1,900,197,964,905
Ethereum      $3,322.69        0.85%    $400,857,294,916
Solana          $142.36       -1.08%     $80,483,198,441
```

---

## 🔥 高级功能

### 自定义分析主题
```python
# 分析任何主题
betta.analyze(
    topic="DeFi生态系统分析",
    coin_id=None,  # 不需要特定币种
    save_report=True
)
```

### 程序化调用

创建自己的分析脚本:
```python
# my_analysis.py
from cryptowatch import CryptoWatch

def analyze_top_coins():
    """分析市值前10的加密货币"""
    betta = CryptoWatch()
    
    top_coins = [
        ("Bitcoin", "bitcoin"),
        ("Ethereum", "ethereum"),
        ("BNB", "binancecoin"),
        ("Solana", "solana"),
        ("XRP", "ripple")
    ]
    
    for name, coin_id in top_coins:
        print(f"\n分析 {name}...\n")
        betta.analyze(name, coin_id)
        print("="*70)

if __name__ == "__main__":
    analyze_top_coins()
```

### 定时任务

使用cron或其他调度工具定期分析:
```bash
# crontab示例 - 每天早上9点分析
0 9 * * * cd /path/to/cryptowatch && python cryptowatch.py
```

---

## ❓ 常见问题

### Q1: API调用失败怎么办?

**A**: 检查以下几点:
1. ✅ API密钥是否正确
2. ✅ 网络连接是否正常
3. ✅ API额度是否用尽
```python
# 调试模式
import os
print(os.getenv("DEEPSEEK_API_KEY"))  # 检查密钥
```

### Q2: 如何分析其他币种?

**A**: 使用CoinGecko的币种ID:
```python
# 查看支持的币种
# 访问: https://www.coingecko.com/

# 示例
betta.analyze("Cardano", "cardano")
betta.analyze("Polkadot", "polkadot")
betta.analyze("Chainlink", "chainlink")
```

### Q3: 报告保存在哪里?

**A**: 默认保存在`reports/`目录:
```bash
# 查看所有报告
ls -lh reports/

# 查看最新报告
ls -lt reports/ | head -5
```

### Q4: 如何关闭报告生成?

**A**: 设置`save_report=False`:
```python
result = betta.analyze(
    topic="Ethereum",
    coin_id="ethereum",
    save_report=False  # 不保存报告
)
```

### Q5: 分析太慢怎么办?

**A**: 几个优化建议:

1. **使用快速检查**
```python
   # 不需要完整分析时
   betta.quick_market_check("bitcoin")
```

2. **减少分析Agent数量**
```python
   # 修改analysis_coordinator.py
   # 只保留需要的Analyst
```

3. **调整LLM参数**
```python
   # 减少max_tokens
   response = self.client.chat.completions.create(
       model="deepseek-chat",
       messages=[...],
       max_tokens=500  # 减少生成长度
   )
```

---

## 💡 最佳实践

### 1. 定期备份报告
```bash
# 创建备份脚本
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf reports_backup_$DATE.tar.gz reports/
```

### 2. 组织报告文件
```bash
# 按月份组织
mkdir -p reports/2026/01
mv reports/analysis_202601*.md reports/2026/01/
```

### 3. 批量分析
```python
def batch_analyze(coin_list):
    """批量分析多个币种"""
    betta = CryptoWatch()
    
    results = {}
    for name, coin_id in coin_list:
        try:
            result = betta.analyze(name, coin_id)
            results[name] = result
        except Exception as e:
            print(f"❌ {name} 分析失败: {e}")
            continue
    
    return results
```

### 4. 错误处理
```python
try:
    result = betta.analyze("Ethereum", "ethereum")
except Exception as e:
    print(f"分析失败: {e}")
    # 发送通知或记录日志
```

### 5. 结果验证
```python
# 检查分析结果的质量
if result and 'analyses' in result:
    analyses = result['analyses']
    
    # 确保所有分析都完成
    if all(key in analyses for key in ['market', 'sentiment', 'risk']):
        print("✅ 分析完整")
    else:
        print("⚠️ 分析不完整")
```

---

## 🛠️ 故障排除

### 问题: 模块导入失败
```bash
# 解决方案: 确保在正确的目录
cd /path/to/cryptowatch
source venv/bin/activate
python -c "import cryptowatch"
```

### 问题: API超时
```python
# 增加超时时间
response = requests.get(url, timeout=30)  # 默认10秒
```

### 问题: 内存不足
```python
# 减少数据收集量
news_data = self.news_agent.search_news(topic, max_results=3)  # 减少为3
```

---

## 📊 使用技巧

### 技巧1: 自定义Prompt

修改`analysis_coordinator.py`中的Prompt模板:
```python
prompt = f"""你是{self.role}。

[自定义你的分析要求]

数据: {data}

请分析: [你想要的分析维度]
"""
```

### 技巧2: 添加数据验证
```python
def validate_data(data):
    """验证数据完整性"""
    required_keys = ['topic', 'timestamp', 'data_sources']
    return all(key in data for key in required_keys)
```

### 技巧3: 导出其他格式
```python
import json

# 导出JSON
with open('result.json', 'w') as f:
    json.dump(result, f, indent=2)
```

---

## 🎓 学习资源

### 推荐阅读

1. **Multi-Agent系统**
   - [LangGraph文档](https://langchain-ai.github.io/langgraph/)
   - [AutoGen教程](https://microsoft.github.io/autogen/)

2. **加密货币分析**
   - [CoinGecko指南](https://www.coingecko.com/learn)
   - [DeFi数据分析](https://defillama.com/)

3. **Python最佳实践**
   - [PEP 8风格指南](https://pep8.org/)
   - [异步编程指南](https://docs.python.org/3/library/asyncio.html)

### 社区支持

- 💬 GitHub Issues
- 📧 Email支持
- 🌐 技术博客

---

## 📝 更新日志

### v1.0.0 (2026-01-18)

- ✅ 初始版本发布
- ✅ 三层架构实现
- ✅ Multi-Agent协作
- ✅ 自动报告生成

---

## 🎯 下一步

掌握基础后,可以尝试:

1. ⭐ 添加自己的数据源
2. ⭐ 创建自定义Agent
3. ⭐ 优化分析算法
4. ⭐ 构建Web界面
5. ⭐ 集成实时监控

---

**祝你使用愉快! 🚀**

如有问题,欢迎反馈:
- 📧 Email: your.email@example.com
- 💬 GitHub: @your-username