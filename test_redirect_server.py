#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        print(f"请求路径: {path}")
        print(f"查询参数: {query_params}")
        
        # 检查是否是需要重定向的路径
        if path.endswith('.html') and 'lang' in query_params:
            lang = query_params['lang'][0]
            
            # 构建新的重定向路径
            if path.startswith('/'):
                new_path = f"/{lang}{path}"
            else:
                new_path = f"/{lang}/{path}"
            
            print(f"重定向到: {new_path}")
            
            # 检查目标文件是否存在
            target_file = new_path.lstrip('/')
            if os.path.exists(target_file):
                self.send_response(301)
                self.send_header('Location', new_path)
                self.end_headers()
                return
            else:
                print(f"目标文件不存在: {target_file}")
        
        # 默认处理
        super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    
    with socketserver.TCPServer(("", PORT), RedirectHandler) as httpd:
        print(f"测试服务器启动在 http://localhost:{PORT}")
        print("测试URL示例:")
        print(f"  http://localhost:{PORT}/knowledge/01-beginners-guide.html?lang=en")
        print(f"  http://localhost:{PORT}/knowledge/01-beginners-guide.html?lang=zh")
        print("按 Ctrl+C 停止服务器")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")