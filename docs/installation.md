# 安装指南

## 系统要求

- Python 3.11 或更高版本
- PostgreSQL 15 或更高版本
- 2GB 以上内存

## 安装步骤

### 1. 克隆仓库
```bash
git clone https://github.com/hanxiao199001/CryptoWatch.git
cd CryptoWatch
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 配置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，填入必要的 API 密钥
```

### 5. 初始化数据库
```bash
# 根据你的项目实际情况调整
python scripts/init_db.py
```

### 6. 运行项目
```bash
python app.py
```

## 常见问题

### 安装依赖失败

确保 pip 是最新版本：
```bash
pip install --upgrade pip
```

### 数据库连接失败

检查 PostgreSQL 是否正在运行，并确认 .env 中的配置正确。
