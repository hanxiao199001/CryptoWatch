"""pytest 配置文件"""
import pytest

@pytest.fixture
def sample_crypto_data():
    """示例加密货币数据"""
    return {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000.0
    }
