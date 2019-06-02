"""
这里需要先从app.py中引入我们装饰器
然后把当前函数导出去
"""
from app.app import app


@app.route('/')
def hello_world():
    return 'Hello World!'
