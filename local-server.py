#!/usr/bin/env python3
"""
BirdAiSnap 本地开发服务器
支持多语言重定向和智能下载功能
"""

import http.server
import socketserver
import os
import sys
import webbrowser
import threading
import time
from urllib.parse import urlparse, parse_qs

class BirdAiSnapServer(http.server.SimpleHTTPRequestHandler):
    """自定义HTTP服务器处理器"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """处理GET请求"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        # 记录请求
        print(f"🌐 {self.client_address[0]} -> {self.path}")
        
        # 处理根路径
        if path == '/':
            path = '/index.html'
        
        file_path = '.' + path
        
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 文件存在，正常处理
            super().do_GET()
        else:
            # 文件不存在，检查是否需要重定向
            self.handle_missing_file(path, query_params)
    
    def handle_missing_file(self, path, query_params):
        """处理不存在的文件"""
        # 检查是否是语言重定向请求
        if 'lang' in query_params:
            print(f"🔄 语言重定向: {path} -> 404.html")
            self.serve_404_page()
        else:
            # 普通404
            self.send_error(404, "File not found")
    
    def serve_404_page(self):
        """提供404页面"""
        self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        try:
            with open('404.html', 'r', encoding='utf-8') as f:
                content = f.read()
            self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            # 如果404.html不存在，返回简单的404页面
            self.wfile.write(b'''<html>
<head>
    <title>404 - Page Not Found</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page could not be found.</p>
    <a href="/">Return to Home</a>
</body>
</html>''')
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] {format % args}")

def check_environment():
    """检查运行环境"""
    print("🔍 检查运行环境...")
    
    # 检查是否在项目根目录
    if not os.path.exists('index.html'):
        print("❌ 错误: 请在项目根目录运行此脚本")
        print("   项目根目录应包含 index.html 文件")
        return False
    
    # 检查必要文件
    required_files = ['smart-download.js', 'script.js', 'styles.css']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️  警告: 缺少文件 {', '.join(missing_files)}")
        print("   某些功能可能无法正常工作")
    
    print("✅ 环境检查完成")
    return True

def find_available_port(start_port=8000):
    """查找可用端口"""
    import socket
    
    for port in range(start_port, start_port + 10):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return port
        except OSError:
            continue
    
    return None

def open_browser(url, delay=1):
    """延迟打开浏览器"""
    def _open():
        time.sleep(delay)
        try:
            webbrowser.open(url)
            print(f"🌐 已自动打开浏览器: {url}")
        except Exception as e:
            print(f"⚠️  无法自动打开浏览器: {e}")
    
    threading.Thread(target=_open, daemon=True).start()

def main():
    """主函数"""
    print("🚀 BirdAiSnap 本地开发服务器")
    print("=" * 40)
    
    # 检查环境
    if not check_environment():
        sys.exit(1)
    
    # 查找可用端口
    port = find_available_port()
    if not port:
        print("❌ 错误: 无法找到可用端口 (8000-8009)")
        sys.exit(1)
    
    # 启动服务器
    try:
        with socketserver.TCPServer(("", port), BirdAiSnapServer) as httpd:
            print(f"🌐 服务器启动成功!")
            print(f"📍 地址: http://localhost:{port}")
            print(f"📁 目录: {os.getcwd()}")
            print()
            print("🔗 主要页面:")
            print(f"   • 主页: http://localhost:{port}/")
            print(f"   • 鸟类应用: http://localhost:{port}/bird-app.html")
            print(f"   • 岩石应用: http://localhost:{port}/rock-app.html")
            print(f"   • 测试页面: http://localhost:{port}/test-smart-download.html")
            print()
            print("💡 提示:")
            print("   • 按 Ctrl+C 停止服务器")
            print("   • 修改文件后刷新浏览器即可看到更改")
            print("   • 支持多语言重定向和智能下载功能")
            print()
            
            # 自动打开浏览器
            open_browser(f"http://localhost:{port}")
            
            print("🔄 服务器运行中...")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except Exception as e:
        print(f"❌ 服务器启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
