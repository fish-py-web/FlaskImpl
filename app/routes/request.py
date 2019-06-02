import json

from app.app import app
from flask import request

"""
解析请求报文

flask中的request对象是import后动态绑定的
竟然不是作为路由函数的参数，这种写法太古怪了吧
"""
@app.route('/req')
def request_handler():
    req = {}

    # 获得请求路径
    req['path'] = request.path

    # 获得请求方法
    req['method'] = request.method

    # 获得请求url
    req['url'] = request.url

    return json.dumps(req)

"""
解析请求头
"""
@app.route('/req/headers')
def headers_handler():
    headers = {}
    for key, value in request.headers.items():
        headers[key] = value
    return json.dumps(headers)

