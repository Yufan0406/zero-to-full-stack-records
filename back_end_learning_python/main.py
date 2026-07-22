# 手搓一个API接口，用于获取页面信息

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    'heroTitle': '关于我',
    'heroSubTitle': '项目，创意，灵感，心得，我的作品',
}

class Handler(BaseHTTPRequestHandler):
    # 请求处理类，此处主要处理GET请求
    def do_GET(self):
        if self.path == '/api/profile': # 检查请求路径是否为/api/profile
            self.send_response(200) # 状态行
            self.send_header('Content-Type', 'application/json') # 响应头
            self.end_headers() # 结束响应头，对应空行，引出响应体
            body = json.dumps(profile, ensure_ascii=False)
            self.wfile.write(body.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

print('后端已经启动：http://localhost:8000/api/profile') # 选择
server = HTTPServer(('', 8000), Handler) # 设置一个服务器，监听8000端口（习惯性设置，实际上随意设置一个没占用的端口即可），使用Handler类处理请求
server.serve_forever()
