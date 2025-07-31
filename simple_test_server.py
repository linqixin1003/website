#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import os

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL和查询参数
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        print(f"请求路径: {path}")
        print(f"查询参数: {query_params}")
        
        # 检查是否是knowledge文章的重定向请求
        if path.startswith('/knowledge/') and path.endswith('.html'):
            # 获取文章文件名
            article_name = os.path.basename(path)
            
            # 获取语言参数
            lang = query_params.get('lang', ['en'])[0]
            
            # 构建重定向URL
            redirect_url = f"/{lang}/knowledge/{article_name}"
            
            print(f"重定向: {self.path} -> {redirect_url}")
            
            # 发送重定向响应
            self.send_response(302)
            self.send_header('Location', redirect_url)
            self.end_headers()
            return
        
        # 对于其他请求，使用默认处理
        super().do_GET()

if __name__ == "__main__":
    PORT = 8002
    with socketserver.TCPServer(("", PORT), RedirectHandler) as httpd:
        print(f"测试服务器启动在端口 {PORT}")
        print(f"访问: http://localhost:{PORT}")
        print(f"测试重定向: http://localhost:{PORT}/knowledge/01-beginners-guide.html?lang=en")
        print(f"测试直接访问: http://localhost:{PORT}/en/knowledge/01-beginners-guide.html")
        httpd.serve_forever()