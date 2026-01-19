"""
CryptoWatch - 完整的Multi-Agent舆情分析系统
整合所有组件,提供完整的分析服务
"""

import os
from datetime import datetime
from data_agents import DataAggregator
from analysis_coordinator import AnalysisCoordinator


class CryptoWatch:
    """
    CryptoWatch 主系统
    完整的Multi-Agent舆情分析平台
    """
    
    def __init__(self):
        self._print_banner()
        
        print("\n🚀 系统初始化中...\n")
        
        # 初始化组件
        self.data_aggregator = DataAggregator()
        self.analysis_coordinator = AnalysisCoordinator()
        
        print("="*70)
        print("✅ CryptoWatch 系统就绪!")
        print("="*70 + "\n")
    
    def _print_banner(self):
        """打印系统标题"""
        banner = """
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                    🐟 CryptoWatch v1.0                            ║
║                                                                      ║
║              Multi-Agent 舆情分析系统                                 ║
║                                                                      ║
║     📊 Web3数据  |  📰 新闻搜索  |  💬 社交分析  |  📝 报告生成        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def analyze(self, topic: str, coin_id: str = None, 
                save_report: bool = True):
        """
        完整的分析流程
        
        Args:
            topic: 分析主题
            coin_id: 加密货币ID (可选)
            save_report: 是否保存报告
        """
        print("\n" + "="*70)
        print(f"🎯 开始分析任务: {topic}")
        print(f"⏰ 开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")
        
        # ===== 阶段1: 数据收集 =====
        print("┌" + "─"*68 + "┐")
        print("│" + " "*20 + "【阶段1: 数据收集】" + " "*28 + "│")
        print("└" + "─"*68 + "┘\n")
        
        data = self.data_aggregator.collect_all_data(topic, coin_id)
        
        # ===== 阶段2: 专家分析 =====
        print("\n┌" + "─"*68 + "┐")
        print("│" + " "*20 + "【阶段2: 专家分析】" + " "*28 + "│")
        print("└" + "─"*68 + "┘\n")
        
        analyses = self.analysis_coordinator.conduct_analysis(data, topic)
        
        # ===== 阶段3: 报告生成 =====
        if save_report:
            print("\n┌" + "─"*68 + "┐")
            print("│" + " "*20 + "【阶段3: 报告生成】" + " "*28 + "│")
            print("└" + "─"*68 + "┘\n")
            
            report = self.analysis_coordinator.generate_final_report(
                topic, data, analyses
            )
        
        # ===== 完成 =====
        print("\n" + "="*70)
        print("✅ 分析任务完成!")
        print(f"⏰ 完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")
        
        return {
            "data": data,
            "analyses": analyses,
            "report": report if save_report else None
        }
    
    def quick_market_check(self, coin_id: str):
        """
        快速市场检查
        只获取数据和简单分析,不生成完整报告
        
        Args:
            coin_id: 加密货币ID
        """
        print(f"\n🔍 快速检查: {coin_id}\n")
        
        # 只收集Web3数据
        from web3_data_agent import Web3DataAgent
        agent = Web3DataAgent()
        
        price_data = agent.get_crypto_price(coin_id)
        
        if price_data:
            print("\n📊 市场快照:")
            print("="*70)
            print(f"💰 当前价格: ${price_data['price']:,.2f}")
            print(f"📈 24h变化: {price_data['change_24h']:.2f}%")
            print(f"💎 市值: ${price_data['market_cap']:,.0f}")
            print(f"📊 交易量: ${price_data['volume_24h']:,.0f}")
            print("="*70 + "\n")
        
        return price_data
    
    def compare_projects(self, projects: list):
        """
        对比多个项目
        
        Args:
            projects: [(name, coin_id), ...]
        """
        print("\n" + "="*70)
        print("📊 项目对比分析")
        print("="*70 + "\n")
        
        from web3_data_agent import Web3DataAgent
        agent = Web3DataAgent()
        
        results = []
        
        for name, coin_id in projects:
            data = agent.get_crypto_price(coin_id)
            if data:
                results.append({
                    "name": name,
                    "data": data
                })
        
        # 显示对比
        print("\n📊 对比结果:")
        print("="*70)
        print(f"{'项目':<15} {'价格':>15} {'24h变化':>12} {'市值':>20}")
        print("-"*70)
        
        for r in results:
            d = r["data"]
            print(f"{r['name']:<15} ${d['price']:>14,.2f} "
                  f"{d['change_24h']:>11.2f}% "
                  f"${d['market_cap']:>19,.0f}")
        
        print("="*70 + "\n")
        
        return results


# ========== 主程序 ==========

def main():
    """主程序入口"""
    
    # 创建系统
    betta = CryptoWatch()
    
    # ===== 示例1: 完整分析 =====
    print("\n" + "🔥"*35)
    print("示例1: 完整的Ethereum分析")
    print("🔥"*35)
    
    betta.analyze(
        topic="Ethereum",
        coin_id="ethereum",
        save_report=True
    )
    
    # ===== 示例2: 快速检查 =====
    print("\n" + "⚡"*35)
    print("示例2: 快速市场检查")
    print("⚡"*35)
    
    betta.quick_market_check("bitcoin")
    
    # ===== 示例3: 项目对比 =====
    print("\n" + "📊"*35)
    print("示例3: 项目对比")
    print("📊"*35)
    
    betta.compare_projects([
        ("Bitcoin", "bitcoin"),
        ("Ethereum", "ethereum"),
        ("Solana", "solana"),
        ("Cardano", "cardano")
    ])
    
    # ===== 总结 =====
    print("\n" + "="*70)
    print("🎉 所有示例完成!")
    print("="*70)
    print("\n💡 提示:")
    print("   - 完整分析报告已保存到 reports/ 目录")
    print("   - 你可以修改代码来分析其他项目")
    print("   - 尝试添加更多数据源和分析维度")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
