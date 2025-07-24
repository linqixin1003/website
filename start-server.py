#!/usr/bin/env python3
"""
BirdAiSnap 本地部署脚本
简单的HTTP服务器，用于本地测试和开发
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# 配置
PORT = 8000
HOST = 'localhost'

def main():
    # 确保在项目根目录运行
    if not os.path.exists('index.html'):
        print("❌ 错误: 请在项目根目录运行此脚本")
        print("   项目根目录应包含 index.html 文件")
        sys.exit(1)
    
    # 创建HTTP服务器
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((HOST, PORT), handler) as httpd:
            print(f"🚀 BirdAiSnap 本地服务器启动成功!")
            print(f"📍 服务器地址: http://{HOST}:{PORT}")
            print(f"📁 服务目录: {os.getcwd()}")
            print(f"🌐 主页: http://{HOST}:{PORT}/index.html")
            print(f"🧠 知识中心: http://{HOST}:{PORT}/knowledge.html")
            print("\n💡 提示:")
            print("   - 按 Ctrl+C 停止服务器")
            print("   - 修改文件后刷新浏览器即可看到更改")
            print("   - 服务器会自动处理静态文件")
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://{HOST}:{PORT}')
                print(f"🔗 已自动打开浏览器")
            except:
                print(f"⚠️  无法自动打开浏览器，请手动访问: http://{HOST}:{PORT}")
            
            print(f"\n🔄 服务器运行中...")
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用")
            print(f"💡 请尝试:")
            print(f"   1. 关闭其他使用端口 {PORT} 的程序")
            print(f"   2. 或修改脚本中的 PORT 变量")
        else:
            print(f"❌ 启动服务器失败: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n👋 服务器已停止")
        sys.exit(0)

if __name__ == "__main__":
    main()