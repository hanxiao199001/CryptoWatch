"""
CryptoWatch - 分析协调器
协调多个Agent进行深度分析
"""

import os
import sys
from typing import Dict, List
from openai import OpenAI
from dotenv import load_dotenv

# 导入之前的模块
sys.path.append(os.path.join(os.path.dirname(__file__), '../day7'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../day8'))

from forum_agents import ForumAgent
from report_agent import ReportAgent

load_dotenv()


class MarketAnalystAgent(ForumAgent):
    """市场分析专家"""
    
    def __init__(self):
        super().__init__(
            name="MarketAnalyst",
            role="市场分析专家",
            perspective="关注价格趋势、交易量、市值变化"
        )
    
    def analyze(self, data: Dict) -> str:
        """分析市场数据"""
        print(f"\n📊 {self.name} 正在分析市场数据...\n")
        
        web3_data = data.get("data_sources", {}).get("web3", {})
        
        prompt = f"""你是市场分析专家。

市场数据:
- 价格: ${web3_data.get('price', 0):,.2f}
- 24h变化: {web3_data.get('change_24h', 0):.2f}%
- 市值: ${web3_data.get('market_cap', 0):,.0f}
- 交易量: ${web3_data.get('volume_24h', 0):,.0f}

请分析:
1. 价格趋势
2. 交易活跃度
3. 市场健康度

保持专业,3-4句话。"""

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        
        analysis = response.choices[0].message.content
        print(f"✅ {self.name} 分析完成\n")
        
        return analysis


class SentimentAnalystAgent(ForumAgent):
    """舆情分析专家"""
    
    def __init__(self):
        super().__init__(
            name="SentimentAnalyst",
            role="舆情分析专家",
            perspective="关注社交媒体情绪、新闻舆论、公众态度"
        )
    
    def analyze(self, data: Dict) -> str:
        """分析舆情数据"""
        print(f"\n💬 {self.name} 正在分析舆情...\n")
        
        social_data = data.get("data_sources", {}).get("social", {})
        news_data = data.get("data_sources", {}).get("news", [])
        
        prompt = f"""你是舆情分析专家。

社交媒体数据:
- 整体情绪: {social_data.get('overall_sentiment', 'N/A')}
- 正面占比: {social_data.get('positive_ratio', 0)*100:.1f}%
- 负面占比: {social_data.get('negative_ratio', 0)*100:.1f}%
- 热门关键词: {', '.join(social_data.get('trending_keywords', []))}

新闻标题:
{chr(10).join([f"- {n.get('title', 'N/A')}" for n in news_data[:3]])}

请分析:
1. 公众情绪趋势
2. 潜在舆情风险
3. 关注焦点

保持专业,3-4句话。"""

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        analysis = response.choices[0].message.content
        print(f"✅ {self.name} 分析完成\n")
        
        return analysis


class RiskAnalystAgent(ForumAgent):
    """风险分析专家"""
    
    def __init__(self):
        super().__init__(
            name="RiskAnalyst",
            role="风险分析专家",
            perspective="关注风险因素、波动性、不确定性"
        )
    
    def analyze(self, data: Dict) -> str:
        """分析风险"""
        print(f"\n⚠️  {self.name} 正在评估风险...\n")
        
        web3_data = data.get("data_sources", {}).get("web3", {})
        social_data = data.get("data_sources", {}).get("social", {})
        
        prompt = f"""你是风险分析专家。

市场数据:
- 24h变化: {web3_data.get('change_24h', 0):.2f}%
- 交易量/市值比: {(web3_data.get('volume_24h', 0) / web3_data.get('market_cap', 1) * 100):.2f}%

舆情数据:
- 负面占比: {social_data.get('negative_ratio', 0)*100:.1f}%

请评估:
1. 市场风险等级
2. 主要风险因素
3. 风险应对建议

保持专业,3-4句话。"""

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        
        analysis = response.choices[0].message.content
        print(f"✅ {self.name} 分析完成\n")
        
        return analysis


class AnalysisCoordinator:
    """
    分析协调器
    协调多个专家Agent进行综合分析
    """
    
    def __init__(self):
        print("\n" + "="*70)
        print("🧠 分析协调器启动")
        print("="*70 + "\n")
        
        # 创建专家团队
        self.market_analyst = MarketAnalystAgent()
        self.sentiment_analyst = SentimentAnalystAgent()
        self.risk_analyst = RiskAnalystAgent()
        self.report_agent = ReportAgent()
        
        print("\n✅ 专家团队集结完成\n")
    
    def conduct_analysis(self, data: Dict, topic: str) -> Dict:
        """
        进行综合分析
        
        Args:
            data: 收集到的数据
            topic: 分析主题
        """
        print("="*70)
        print(f"🔍 开始综合分析: {topic}")
        print("="*70)
        
        # 各专家进行分析
        analyses = {
            "market": self.market_analyst.analyze(data),
            "sentiment": self.sentiment_analyst.analyze(data),
            "risk": self.risk_analyst.analyze(data)
        }
        
        # 显示分析结果
        print("\n" + "="*70)
        print("📊 专家分析结果")
        print("="*70 + "\n")
        
        print(f"💼 市场分析:\n{analyses['market']}\n")
        print(f"💬 舆情分析:\n{analyses['sentiment']}\n")
        print(f"⚠️  风险评估:\n{analyses['risk']}\n")
        
        return analyses
    
    def generate_final_report(self, topic: str, data: Dict, analyses: Dict) -> str:
        """
        生成最终报告
        
        Args:
            topic: 分析主题
            data: 原始数据
            analyses: 专家分析结果
        """
        print("="*70)
        print("📝 生成最终报告")
        print("="*70 + "\n")
        
        # 准备报告数据
        research_data = {
            "raw_data": data,
            "expert_analyses": analyses
        }
        
        # 生成综合结论
        conclusion = f"""
【综合分析】

市场层面: {analyses['market'][:100]}...

舆情层面: {analyses['sentiment'][:100]}...

风险层面: {analyses['risk'][:100]}...
"""
        
        # 生成报告
        report = self.report_agent.generate_report(
            topic=f"{topic} - 综合分析报告",
            research_data=research_data,
            forum_conclusion=conclusion
        )
        
        # 保存报告
        filename = self.report_agent.save_report(report, f"{topic}_comprehensive")
        
        print(f"✅ 报告已生成并保存: {filename}\n")
        
        return report


# ========== 测试分析协调器 ==========

if __name__ == "__main__":
    from data_agents import DataAggregator
    
    # 1. 收集数据
    print("\n【阶段1: 数据收集】\n")
    aggregator = DataAggregator()
    data = aggregator.collect_all_data(
        topic="Ethereum",
        coin_id="ethereum"
    )
    
    # 2. 进行分析
    print("\n【阶段2: 专家分析】\n")
    coordinator = AnalysisCoordinator()
    analyses = coordinator.conduct_analysis(data, "Ethereum")
    
    # 3. 生成报告
    print("\n【阶段3: 报告生成】\n")
    report = coordinator.generate_final_report("Ethereum", data, analyses)
    
    print("\n" + "="*70)
    print("🎉 完整分析流程完成!")
    print("="*70)