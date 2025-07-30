#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import urllib.parse
import os
import mimetypes

class FinalRedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)
        
        # 只处理查询参数格式的德语请求重定向
        if 'lang' in query and 'de' in query['lang'] and not path.startswith('/de/'):
            # 提取文件路径
            if path.startswith('/'):
                path = path[1:]  # 移除开头的斜杠
            
            # 构建德语版本的路径
            de_path = f'/de/{path}'
            
            # 检查德语文件是否存在
            file_path = f'de/{path}'
            if os.path.exists(file_path) and os.path.isfile(file_path):
                # 重定向到德语版本（不带查询参数）
                self.send_response(302)
                self.send_header('Location', de_path)
                self.end_headers()
                print(f"重定向: {self.path} -> {de_path}")
                return
        
        # 对于所有其他请求，包括德语子目录的请求，直接提供文件服务
        return super().do_GET()
    
    def end_headers(self):
        # 添加CORS头部以避免跨域问题
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server(port=8000):
    try:
        with socketserver.TCPServer(("", port), FinalRedirectHandler) as httpd:
            print(f"最终重定向服务器运行在 http://localhost:{port}")
            print("支持以下URL格式:")
            print(f"  - http://localhost:{port}/birdwatching/01-getting-started.html?lang=de")
            print(f"  - http://localhost:{port}/de/birdwatching/01-getting-started.html")
            print("特点:")
            print("  - 只重定向查询参数格式到子目录格式")
            print("  - 避免重定向循环")
            print("  - 支持所有静态文件服务")
            print("按 Ctrl+C 停止服务器")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"端口 {port} 已被占用，尝试使用端口 {port + 1}")
            start_server(port + 1)
        else:
            raise

if __name__ == "__main__":
    start_server()