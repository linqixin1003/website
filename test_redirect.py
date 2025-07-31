#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import os

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = urllib.parse.parse_qs(parsed_url.query)
        
        # 检查是否是knowledge文章请求
        if path.startswith('/knowledge/'):
            article_name = path[11:]  # 移除 '/knowledge/' 前缀
            
            # 获取lang参数
            lang = 'en'  # 默认语言
            if 'lang' in query and query['lang']:
                lang = query['lang'][0]
            
            # 构建重定向URL
            redirect_url = f'/{lang}/knowledge/{article_name}'
            
            # 检查目标文件是否存在
            target_file = f'.{redirect_url}'
            if os.path.exists(target_file):
                print(f"重定向: {self.path} -> {redirect_url}")
                self.send_response(302)
                self.send_header('Location', redirect_url)
                self.end_headers()
                return
            else:
                print(f"目标文件不存在: {target_file}")
        
        # 默认处理
        super().do_GET()

PORT = 8001
Handler = RedirectHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器启动在端口 {PORT}")
    print(f"访问: http://localhost:{PORT}")
    print(f"测试重定向: http://localhost:{PORT}/knowledge/01-beginners-guide.html?lang=en")
    httpd.serve_forever()