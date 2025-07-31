#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        print(f"请求路径: {self.path}")
        
        # 检查文件是否存在
        if path == '/':
            path = '/index.html'
        
        file_path = '.' + path
        
        # 如果文件不存在且有lang参数，返回404.html进行重定向处理
        if not os.path.exists(file_path) and 'lang' in query_params:
            print(f"文件不存在，返回404页面进行重定向: {self.path}")
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # 读取404.html文件
            try:
                with open('404.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                # 如果404.html不存在，返回简单的404页面
                self.wfile.write(b'<html><body><h1>404 Not Found</h1></body></html>')
            return
        
        # 对于其他情况，使用默认处理
        super().do_GET()

PORT = 8000

with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"服务器运行在 http://localhost:{PORT}")
    print("支持自定义404重定向")
    httpd.serve_forever()