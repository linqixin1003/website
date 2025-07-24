#!/bin/bash

# BirdAiSnap 本地部署脚本 (Bash版本)
# 适用于 macOS/Linux 系统

PORT=8000
HOST="localhost"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 BirdAiSnap 本地部署脚本${NC}"
echo "=================================="

# 检查是否在项目根目录
if [ ! -f "index.html" ]; then
    echo -e "${RED}❌ 错误: 请在项目根目录运行此脚本${NC}"
    echo "   项目根目录应包含 index.html 文件"
    exit 1
fi

# 检查端口是否被占用
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo -e "${RED}❌ 端口 $PORT 已被占用${NC}"
    echo -e "${YELLOW}💡 请尝试:${NC}"
    echo "   1. 关闭其他使用端口 $PORT 的程序"
    echo "   2. 或修改脚本中的 PORT 变量"
    exit 1
fi

echo -e "${GREEN}✅ 环境检查通过${NC}"
echo ""

# 启动服务器
echo -e "${BLUE}🌐 启动本地服务器...${NC}"
echo -e "${GREEN}📍 服务器地址: http://$HOST:$PORT${NC}"
echo -e "${GREEN}📁 服务目录: $(pwd)${NC}"
echo -e "${GREEN}🌐 主页: http://$HOST:$PORT/index.html${NC}"
echo -e "${GREEN}🧠 知识中心: http://$HOST:$PORT/knowledge.html${NC}"
echo ""
echo -e "${YELLOW}💡 提示:${NC}"
echo "   - 按 Ctrl+C 停止服务器"
echo "   - 修改文件后刷新浏览器即可看到更改"
echo "   - 服务器会自动处理静态文件"
echo ""

# 尝试自动打开浏览器
if command -v open >/dev/null 2>&1; then
    # macOS
    open "http://$HOST:$PORT"
    echo -e "${GREEN}🔗 已自动打开浏览器 (macOS)${NC}"
elif command -v xdg-open >/dev/null 2>&1; then
    # Linux
    xdg-open "http://$HOST:$PORT"
    echo -e "${GREEN}🔗 已自动打开浏览器 (Linux)${NC}"
else
    echo -e "${YELLOW}⚠️  无法自动打开浏览器，请手动访问: http://$HOST:$PORT${NC}"
fi

echo ""
echo -e "${BLUE}🔄 服务器运行中...${NC}"

# 启动Python HTTP服务器
if command -v python3 >/dev/null 2>&1; then
    python3 -m http.server $PORT
elif command -v python >/dev/null 2>&1; then
    python -m http.server $PORT
else
    echo -e "${RED}❌ 错误: 未找到 Python${NC}"
    echo "请安装 Python 3 或 Python 2"
    exit 1
fi