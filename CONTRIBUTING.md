# 贡献指南 Contributing Guide

感谢你对 CryptoWatch 项目的关注！🎉

## 📋 贡献方式

### 报告 Bug 🐛

在 [Issues](https://github.com/hanxiao199001/CryptoWatch/issues) 页面创建新 issue，请包含：

- **问题描述**: 清晰描述遇到的问题
- **复现步骤**: 详细的操作步骤
- **预期行为**: 期望的正确行为
- **实际行为**: 实际发生的错误行为
- **环境信息**: 
  - Python 版本
  - 操作系统
  - 相关依赖版本

### 提出新功能 💡

通过 [Discussions](https://github.com/hanxiao199001/CryptoWatch/discussions) 或 Issues 提出：

- 功能描述和使用场景
- 预期的实现方式
- 可能的技术难点

### 提交代码 🔧

1. **Fork 仓库**
```bash
   # 在 GitHub 页面点击 Fork 按钮
```

2. **克隆到本地**
```bash
   git clone https://github.com/YOUR_USERNAME/CryptoWatch.git
   cd CryptoWatch
```

3. **创建特性分支**
```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
```

4. **进行开发**
   - 编写代码
   - 添加测试
   - 更新文档

5. **提交更改**
```bash
   git add .
   git commit -m "feat: add amazing feature"
```

6. **推送分支**
```bash
   git push origin feature/your-feature-name
```

7. **创建 Pull Request**
   - 在 GitHub 页面点击 "New Pull Request"
   - 填写 PR 描述
   - 等待代码审查

## 📝 代码规范

### Python 代码风格

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范：
```python
# 好的示例
def analyze_sentiment(text: str) -> float:
    """
    分析文本情感
    
    Args:
        text: 待分析的文本
        
    Returns:
        情感得分 (-1.0 到 1.0)
    """
    # 实现代码
    pass
```

### Commit 信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
```
feat: 添加新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整（不影响功能）
refactor: 代码重构
test: 测试相关
chore: 构建/工具链相关
perf: 性能优化
```

**示例**:
```
feat: add Bitcoin price prediction
fix: resolve data fetching timeout issue
docs: update installation guide
```

## 🧪 测试要求

提交代码前请确保：
```bash
# 运行单元测试
pytest tests/

# 代码格式检查
flake8 .

# 类型检查
mypy .
```

## 📚 文档要求

- 为新功能添加使用文档
- 更新相关的 API 文档
- 在代码中添加必要的注释
- 更新 README（如有必要）

## 🔍 代码审查

PR 提交后会进行代码审查，请：

- 及时响应审查意见
- 保持代码简洁清晰
- 确保测试通过
- 解决所有讨论

## 🎯 开发环境设置
```bash
# 1. 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 2. 安装开发依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 如果有

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 填入配置

# 4. 运行测试验证环境
pytest tests/
```

## 💬 社区交流

- **Issues**: 报告 bug 和功能请求
- **Discussions**: 技术讨论和问答
- **Email**: han272624836@gmail.com

## 🙏 感谢

感谢所有为 CryptoWatch 做出贡献的开发者！

---

再次感谢你的贡献！🎉
