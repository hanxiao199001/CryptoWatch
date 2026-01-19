"""
CryptoWatch - 数据Agent集合
整合所有数据源
"""

import os
import sys
import requests
from typing import Dict, List
from datetime import datetime

# 添加路径以导入之前的模块
sys.path.append(os.path.join(os.path.dirname(__file__), '../day9'))
from web3_data_agent import Web3DataAgent


class NewsSearchAgent:
    """
    新闻搜索Agent
    使用Tavily API搜索相关新闻
    """
    
    def __init__(self, api_key: str = None):
        self.name = "NewsAgent"
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")
        self.base_url = "https://api.tavily.com/search"
        
        print(f"📰 {self.name} 已启动 (新闻搜索专家)")
    
    def search_news(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        搜索相关新闻
        
        Args:
            query: 搜索关键词
            max_results: 最大结果数
        """
        if not self.api_key:
            print("⚠️  未设置TAVILY_API_KEY,返回模拟数据")
            return self._mock_news_data(query)
        
        try:
            payload = {
                "api_key": self.api_key,
                "query": query,
                "search_depth": "basic",
                "max_results": max_results
            }
            
            response = requests.post(
                self.base_url, 
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            results = data.get("results", [])
            
            print(f"✅ 找到 {len(results)} 条相关新闻")
            
            return results
            
        except Exception as e:
            print(f"❌ 新闻搜索失败: {e}")
            return self._mock_news_data(query)
    
    def _mock_news_data(self, query: str) -> List[Dict]:
        """模拟新闻数据(用于测试)"""
        return [
            {
                "title": f"{query} - 市场动态分析",
                "url": "https://example.com/news1",
                "content": f"关于{query}的最新市场分析...",
                "score": 0.9
            },
            {
                "title": f"{query} - 行业趋势报告",
                "url": "https://example.com/news2",
                "content": f"{query}相关的行业趋势分析...",
                "score": 0.85
            }
        ]


class SocialSentimentAgent:
    """
    社交媒体舆情Agent
    分析社交媒体情绪
    """
    
    def __init__(self):
        self.name = "SocialAgent"
        print(f"💬 {self.name} 已启动 (社交媒体分析专家)")
    
    def analyze_sentiment(self, topic: str) -> Dict:
        """
        分析主题的社交媒体情绪
        
        Args:
            topic: 分析主题
        """
        print(f"🔍 {self.name} 正在分析 {topic} 的社交媒体情绪...")
        
        # 模拟情绪分析结果
        sentiment_data = {
            "topic": topic,
            "overall_sentiment": "积极",
            "positive_ratio": 0.65,
            "neutral_ratio": 0.25,
            "negative_ratio": 0.10,
            "trending_keywords": [
                "创新", "增长", "机会"
            ],
            "key_opinions": [
                "社区对该项目的技术创新表示认可",
                "投资者关注长期发展潜力",
                "部分用户对短期波动表示担忧"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"✅ {self.name} 分析完成")
        print(f"   整体情绪: {sentiment_data['overall_sentiment']}")
        print(f"   正面占比: {sentiment_data['positive_ratio']*100:.1f}%")
        
        return sentiment_data


class DataAggregator:
    """
    数据聚合器
    统一管理所有数据Agent
    """
    
    def __init__(self):
        print("\n" + "="*70)
        print("📊 数据聚合器启动")
        print("="*70 + "\n")
        
        # 初始化所有数据Agent
        self.web3_agent = Web3DataAgent()
        self.news_agent = NewsSearchAgent()
        self.social_agent = SocialSentimentAgent()
        
        print("\n✅ 所有数据Agent初始化完成\n")
    
    def collect_all_data(self, topic: str, coin_id: str = None) -> Dict:
        """
        收集所有相关数据
        
        Args:
            topic: 分析主题
            coin_id: 加密货币ID (可选)
        """
        print("="*70)
        print(f"📊 开始收集数据: {topic}")
        print("="*70 + "\n")
        
        all_data = {
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "data_sources": {}
        }
        
        # 1. Web3数据 (如果提供了coin_id)
        if coin_id:
            print("📍 收集Web3数据...\n")
            web3_data = self.web3_agent.get_crypto_price(coin_id)
            all_data["data_sources"]["web3"] = web3_data
        
        # 2. 新闻数据
        print("\n📍 收集新闻数据...\n")
        news_data = self.news_agent.search_news(topic, max_results=3)
        all_data["data_sources"]["news"] = news_data
        
        # 3. 社交媒体数据
        print("\n📍 收集社交媒体数据...\n")
        social_data = self.social_agent.analyze_sentiment(topic)
        all_data["data_sources"]["social"] = social_data
        
        print("\n" + "="*70)
        print("✅ 数据收集完成")
        print("="*70 + "\n")
        
        return all_data


# ========== 测试数据Agent ==========

if __name__ == "__main__":
    # 创建数据聚合器
    aggregator = DataAggregator()
    
    # 测试数据收集
    print("\n📍 测试: 收集Ethereum相关数据\n")
    data = aggregator.collect_all_data(
        topic="Ethereum",
        coin_id="ethereum"
    )
    
    # 显示收集到的数据
    print("\n📊 收集到的数据概览:")
    print("="*70)
    
    if "web3" in data["data_sources"]:
        web3 = data["data_sources"]["web3"]
        print(f"\n💰 Web3数据:")
        print(f"   价格: ${web3.get('price', 0):,.2f}")
        print(f"   24h变化: {web3.get('change_24h', 0):.2f}%")
    
    if "news" in data["data_sources"]:
        news = data["data_sources"]["news"]
        print(f"\n📰 新闻数据: {len(news)} 条")
        for i, item in enumerate(news[:2], 1):
            print(f"   {i}. {item.get('title', 'N/A')}")
    
    if "social" in data["data_sources"]:
        social = data["data_sources"]["social"]
        print(f"\n💬 社交媒体:")
        print(f"   整体情绪: {social.get('overall_sentiment', 'N/A')}")
        print(f"   正面占比: {social.get('positive_ratio', 0)*100:.1f}%")
    
    print("\n" + "="*70)