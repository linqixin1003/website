#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import urllib.parse
import os
import re

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)
        
        # 检查是否是查询参数格式的德语请求
        if 'lang' in query and 'de' in query['lang']:
            # 提取文件路径
            if path.startswith('/'):
                path = path[1:]  # 移除开头的斜杠
            
            # 构建德语版本的路径
            de_path = f'/de/{path}'
            
            # 检查德语文件是否存在
            file_path = f'de/{path}'
            if os.path.exists(file_path):
                # 重定向到德语版本
                self.send_response(302)
                self.send_header('Location', de_path)
                self.end_headers()
                return
        
        # 对于德语子目录的请求，直接提供文件服务
        if path.startswith('/de/'):
            # 移除开头的斜杠并提供文件
            file_path = path[1:]  # 移除开头的斜杠
            if os.path.exists(file_path):
                # 设置正确的路径并调用父类方法
                self.path = '/' + file_path
                return super().do_GET()
        
        # 其他请求正常处理
        return super().do_GET()

def start_server(port=8000):
    try:
        with socketserver.TCPServer(("", port), RedirectHandler) as httpd:
            print(f"服务器运行在 http://localhost:{port}")
            print("支持以下URL格式:")
            print(f"  - http://localhost:{port}/birdwatching/01-getting-started.html?lang=de")
            print(f"  - http://localhost:{port}/de/birdwatching/01-getting-started.html")
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