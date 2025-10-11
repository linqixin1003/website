#!/bin/bash

# BirdAiSnap 快速启动脚本
# 最简单的本地部署方式

echo "🚀 BirdAiSnap 快速启动"
echo "======================"

# 检查Python
if command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON="python"
else
    echo "❌ 未找到Python，请先安装Python"
    exit 1
fi

# 检查项目文件
if [ ! -f "index.html" ]; then
    echo "❌ 请在项目根目录运行此脚本"
    exit 1
fi

# 查找可用端口
PORT=8000
while lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; do
    PORT=$((PORT + 1))
done

echo "🌐 启动服务器在端口 $PORT"
echo "📍 访问地址: http://localhost:$PORT"
echo "💡 按 Ctrl+C 停止服务器"
echo ""

# 自动打开浏览器
(sleep 2 && open "http://localhost:$PORT" 2>/dev/null || true) &

# 启动服务器
$PYTHON -m http.server $PORT
