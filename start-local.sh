#!/bin/bash

# BirdAiSnap 本地部署脚本 (增强版)
# 支持多平台和智能功能检测

set -e  # 遇到错误立即退出

# 配置
PORT=8000
HOST="localhost"
PROJECT_NAME="BirdAiSnap"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "${PURPLE}🚀 $PROJECT_NAME 本地部署脚本${NC}"
    echo "=================================="
}

# 检查项目环境
check_project() {
    print_info "检查项目环境..."
    
    if [ ! -f "index.html" ]; then
        print_error "请在项目根目录运行此脚本"
        echo "   项目根目录应包含 index.html 文件"
        exit 1
    fi
    
    # 检查关键文件
    local missing_files=()
    
    if [ ! -f "smart-download.js" ]; then
        missing_files+=("smart-download.js")
    fi
    
    if [ ! -f "script.js" ]; then
        missing_files+=("script.js")
    fi
    
    if [ ! -f "styles.css" ]; then
        missing_files+=("styles.css")
    fi
    
    if [ ${#missing_files[@]} -gt 0 ]; then
        print_warning "缺少文件: ${missing_files[*]}"
        echo "   某些功能可能无法正常工作"
    fi
    
    print_success "项目环境检查完成"
}

# 检查端口占用
check_port() {
    print_info "检查端口 $PORT..."
    
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
        print_error "端口 $PORT 已被占用"
        echo ""
        print_info "解决方案:"
        echo "   1. 关闭其他使用端口 $PORT 的程序"
        echo "   2. 或修改脚本中的 PORT 变量"
        echo "   3. 或使用不同的端口"
        echo ""
        
        # 尝试找到可用端口
        local new_port=$PORT
        while [ $new_port -lt $((PORT + 10)) ]; do
            new_port=$((new_port + 1))
            if ! lsof -Pi :$new_port -sTCP:LISTEN -t >/dev/null 2>&1; then
                print_info "建议使用端口: $new_port"
                read -p "是否使用端口 $new_port? (y/n): " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    PORT=$new_port
                    break
                fi
            fi
        done
        
        if [ $PORT -eq 8000 ]; then
            exit 1
        fi
    fi
    
    print_success "端口 $PORT 可用"
}

# 检查Python环境
check_python() {
    print_info "检查Python环境..."
    
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD="python3"
        print_success "找到 Python3"
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD="python"
        print_success "找到 Python"
    else
        print_error "未找到 Python"
        echo "请安装 Python 3 或 Python 2"
        exit 1
    fi
}

# 启动服务器
start_server() {
    print_info "启动本地服务器..."
    
    echo ""
    print_success "服务器信息:"
    echo "   📍 地址: http://$HOST:$PORT"
    echo "   📁 目录: $(pwd)"
    echo ""
    
    print_success "主要页面:"
    echo "   • 主页: http://$HOST:$PORT/"
    echo "   • 鸟类应用: http://$HOST:$PORT/bird-app.html"
    echo "   • 岩石应用: http://$HOST:$PORT/rock-app.html"
    echo "   • 测试页面: http://$HOST:$PORT/test-smart-download.html"
    echo ""
    
    print_info "功能特性:"
    echo "   • 多语言支持 (中/英/德/法/西/意/葡/日/韩/俄)"
    echo "   • 智能下载 (iOS/Android 自动识别)"
    echo "   • 移动端优化"
    echo "   • 实时重载 (修改文件后刷新浏览器)"
    echo ""
    
    print_info "控制命令:"
    echo "   • 停止服务器: Ctrl+C"
    echo "   • 查看日志: 终端输出"
    echo ""
    
    # 自动打开浏览器
    open_browser
    
    print_info "服务器运行中..."
    echo "=================================="
    
    # 启动Python HTTP服务器
    $PYTHON_CMD -m http.server $PORT
}

# 自动打开浏览器
open_browser() {
    local url="http://$HOST:$PORT"
    
    # 延迟打开浏览器，避免服务器启动冲突
    (
        sleep 2
        if command -v open >/dev/null 2>&1; then
            # macOS
            open "$url"
            print_success "已自动打开浏览器 (macOS)"
        elif command -v xdg-open >/dev/null 2>&1; then
            # Linux
            xdg-open "$url"
            print_success "已自动打开浏览器 (Linux)"
        elif command -v start >/dev/null 2>&1; then
            # Windows (Git Bash)
            start "$url"
            print_success "已自动打开浏览器 (Windows)"
        else
            print_warning "无法自动打开浏览器，请手动访问: $url"
        fi
    ) &
}

# 显示帮助信息
show_help() {
    echo "用法: $0 [选项]"
    echo ""
    echo "选项:"
    echo "  -h, --help     显示此帮助信息"
    echo "  -p, --port     指定端口号 (默认: 8000)"
    echo "  -n, --no-open  不自动打开浏览器"
    echo "  -q, --quiet    静默模式"
    echo ""
    echo "示例:"
    echo "  $0                # 使用默认设置启动"
    echo "  $0 -p 8080        # 使用端口 8080"
    echo "  $0 --no-open      # 不自动打开浏览器"
}

# 主函数
main() {
    # 解析命令行参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -p|--port)
                PORT="$2"
                shift 2
                ;;
            -n|--no-open)
                NO_OPEN=true
                shift
                ;;
            -q|--quiet)
                QUIET=true
                shift
                ;;
            *)
                print_error "未知选项: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    # 静默模式设置
    if [ "$QUIET" = true ]; then
        exec >/dev/null 2>&1
    fi
    
    print_header
    
    # 执行检查
    check_project
    check_port
    check_python
    
    # 启动服务器
    start_server
}

# 捕获中断信号
trap 'echo -e "\n${YELLOW}👋 服务器已停止${NC}"; exit 0' INT

# 运行主函数
main "$@"
