"""
设置响应报文

这种写法太古怪了，还是express中的舒服
而且IDE没有智能提醒，太难受了
"""
import json

from app.app import app
from flask import make_response


@app.route('/res')
def response_handler():
    # 创建响应报文对象
    response = make_response(json.dumps({'name': 'Jon Snow'}))

    # 设置cookie
    response.set_cookie('token', 'abc123')

    # 设置headers
    response.headers['server'] = 'flask'
    response.headers['Content-Type'] = 'application/json'
    return response
