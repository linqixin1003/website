#!/usr/bin/env python3
import http.server
import socketserver
import urllib.parse
import os
from pathlib import Path

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        # 检查是否有lang参数
        if 'lang' in query_params:
            lang = query_params['lang'][0]
            
            # 支持的语言列表
            supported_languages = ['en', 'zh', 'ko', 'ja', 'de', 'fr', 'es', 'it', 'pt', 'ru']
            
            if lang in supported_languages and lang != 'en':
                # 构建德语子目录路径
                if path.startswith('/'):
                    path = path[1:]  # 移除开头的斜杠
                
                # 构建新的路径
                new_path = f'/{lang}/{path}'
                
                # 检查文件是否存在
                file_path = Path(f'.{new_path}')
                if file_path.exists() and file_path.is_file():
                    # 重定向到德语版本
                    self.send_response(302)
                    self.send_header('Location', new_path)
                    self.end_headers()
                    return
        
        # 检查是否是德语子目录访问，如果是，直接提供文件
        if path.startswith('/de/'):
            # 移除开头的斜杠并检查文件
            file_path = Path(f'.{path}')
            if file_path.exists() and file_path.is_file():
                # 直接提供文件
                super().do_GET()
                return
        
        # 默认处理
        super().do_GET()

def run_server(port=8000):
    handler = RedirectHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"服务器运行在 http://localhost:{port}")
            print("支持以下URL格式:")
            print(f"  - http://localhost:{port}/birdwatching/01-getting-started.html?lang=de")
            print(f"  - http://localhost:{port}/de/birdwatching/01-getting-started.html")
            print("按 Ctrl+C 停止服务器")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"端口 {port} 已被占用，尝试使用端口 {port + 1}")
            run_server(port + 1)
        else:
            print(f"启动服务器时出错: {e}")

if __name__ == "__main__":
    run_server()