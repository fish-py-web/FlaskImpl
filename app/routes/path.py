"""
配置动态路由
"""
from app.app import app


@app.route('/users/<name>')
def path(name):
    return 'Hello ' + name
