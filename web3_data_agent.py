"""
Web3 数据Agent
学习目标:
1. 连接区块链API
2. 获取加密货币数据
3. 分析DeFi协议
"""

import os
import requests
from typing import Dict, List
from datetime import datetime
import json

class Web3DataAgent:
    """
    Web3数据Agent
    专门处理区块链和加密货币数据
    """
    
    def __init__(self, name: str = "Web3Agent"):
        self.name = name
        
        # CoinGecko API (免费,无需API key)
        self.coingecko_base = "https://api.coingecko.com/api/v3"
        
        print(f"🔗 {self.name} 已启动 (Web3数据专家)")
    
    def get_crypto_price(self, coin_id: str = "bitcoin") -> Dict:
        """
        获取加密货币价格
        
        Args:
            coin_id: 币种ID (bitcoin, ethereum, etc.)
        """
        try:
            url = f"{self.coingecko_base}/simple/price"
            params = {
                "ids": coin_id,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_market_cap": "true",
                "include_24hr_vol": "true"
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if coin_id in data:
                result = {
                    "coin": coin_id,
                    "price": data[coin_id]["usd"],
                    "change_24h": data[coin_id].get("usd_24h_change", 0),
                    "market_cap": data[coin_id].get("usd_market_cap", 0),
                    "volume_24h": data[coin_id].get("usd_24h_vol", 0),
                    "timestamp": datetime.now().isoformat()
                }
                
                print(f"✅ 获取 {coin_id} 价格成功: ${result['price']:,.2f}")
                return result
            else:
                print(f"❌ 未找到 {coin_id} 的数据")
                return {}
                
        except Exception as e:
            print(f"❌ 获取价格失败: {e}")
            return {}
    
    def get_trending_coins(self, limit: int = 7) -> List[Dict]:
        """获取热门币种"""
        try:
            url = f"{self.coingecko_base}/search/trending"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            trending = []
            for item in data.get("coins", [])[:limit]:
                coin = item.get("item", {})
                trending.append({
                    "name": coin.get("name"),
                    "symbol": coin.get("symbol"),
                    "market_cap_rank": coin.get("market_cap_rank"),
                    "price_btc": coin.get("price_btc")
                })
            
            print(f"✅ 获取 {len(trending)} 个热门币种")
            return trending
            
        except Exception as e:
            print(f"❌ 获取热门币种失败: {e}")
            return []
    
    def get_defi_market_data(self) -> Dict:
        """获取DeFi市场数据"""
        try:
            url = f"{self.coingecko_base}/global/decentralized_finance_defi"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json().get("data", {})
            
            result = {
                "defi_market_cap": data.get("defi_market_cap", 0),
                "eth_market_cap": data.get("eth_market_cap", 0),
                "defi_to_eth_ratio": data.get("defi_to_eth_ratio", 0),
                "trading_volume_24h": data.get("trading_volume_24h", 0),
                "defi_dominance": data.get("defi_dominance", 0),
                "top_coin_name": data.get("top_coin_name", ""),
                "timestamp": datetime.now().isoformat()
            }
            
            print(f"✅ 获取DeFi市场数据成功")
            defi_cap = float(result.get('defi_market_cap', 0))
            vol_24h = float(result.get('trading_volume_24h', 0))
            print(f"   DeFi市值: ${defi_cap:,.0f}")
            print(f"   24h交易量: ${vol_24h:,.0f}")
            
            return result
            
        except Exception as e:
            print(f"❌ 获取DeFi数据失败: {e}")
            return {}
    
    def analyze_coin(self, coin_id: str) -> str:
        """
        分析单个币种
        返回分析文本供其他Agent使用
        """
        print(f"\n📊 分析 {coin_id}...\n")
        
        # 获取价格数据
        price_data = self.get_crypto_price(coin_id)
        
        if not price_data:
            return f"无法获取 {coin_id} 的数据"
        
        # 构建分析文本
        analysis = f"""
【{coin_id.upper()} 市场数据】
当前价格: ${price_data['price']:,.2f}
24小时变化: {price_data['change_24h']:.2f}%
市值: ${price_data['market_cap']:,.0f}
24小时交易量: ${price_data['volume_24h']:,.0f}

市场趋势: {'📈 上涨' if price_data['change_24h'] > 0 else '📉 下跌'}
波动程度: {'高波动' if abs(price_data['change_24h']) > 5 else '中等波动' if abs(price_data['change_24h']) > 2 else '低波动'}
"""
        
        return analysis.strip()
    
    def get_market_overview(self) -> str:
        """获取市场概览"""
        print(f"\n🌐 获取市场概览...\n")
        
        # 1. 获取主流币数据
        btc = self.get_crypto_price("bitcoin")
        eth = self.get_crypto_price("ethereum")
        
        # 2. 获取DeFi数据
        defi = self.get_defi_market_data()
        
        # 3. 获取热门币种
        trending = self.get_trending_coins(5)
        
        # 构建概览
        overview = f"""
【加密货币市场概览】

主流币种:
- Bitcoin: ${btc.get('price', 0):,.2f} ({btc.get('change_24h', 0):.2f}%)
- Ethereum: ${eth.get('price', 0):,.2f} ({eth.get('change_24h', 0):.2f}%)

DeFi生态:
- DeFi总市值: ${defi.get('defi_market_cap', 0):,.0f}
- 24h交易量: ${defi.get('trading_volume_24h', 0):,.0f}
- DeFi占比: {defi.get('defi_dominance', 0):.2f}%

热门币种:
"""
        
        for i, coin in enumerate(trending, 1):
            overview += f"{i}. {coin['name']} ({coin['symbol']}) - 市值排名 #{coin.get('market_cap_rank', 'N/A')}\n"
        
        return overview.strip()


# ========== 测试Web3 Agent ==========

if __name__ == "__main__":
    # 创建Agent
    agent = Web3DataAgent()
    
    print("\n" + "="*70)
    print("🧪 测试 Web3 数据获取")
    print("="*70 + "\n")
    
    # 测试1: 获取BTC价格
    print("📍 测试1: 获取Bitcoin价格")
    btc_data = agent.get_crypto_price("bitcoin")
    print(f"结果: {json.dumps(btc_data, indent=2)}\n")
    
    # 测试2: 获取热门币种
    print("📍 测试2: 获取热门币种")
    trending = agent.get_trending_coins(5)
    for coin in trending:
        print(f"  - {coin['name']} ({coin['symbol']})")
    print()
    
    # 测试3: 获取DeFi数据
    print("📍 测试3: 获取DeFi市场数据")
    defi = agent.get_defi_market_data()
    print()
    
    # 测试4: 完整市场概览
    print("📍 测试4: 市场概览")
    print("="*70)
    overview = agent.get_market_overview()
    print(overview)
    print("="*70)