# 测试说明

## 运行测试
```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/unit/

# 查看覆盖率
pytest --cov=. --cov-report=html
```

## 测试结构

- `unit/` - 单元测试
- `integration/` - 集成测试
- `conftest.py` - pytest 配置
