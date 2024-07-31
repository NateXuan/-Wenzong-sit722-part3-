# 指定目标架构为x86_64
FROM --platform=linux/amd64 python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制 app 目录中的所有内容（包括 main.py）
COPY app/ .

# 暴露端口
EXPOSE 8000

# 运行 uvicorn 以启动 FastAPI 应用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
