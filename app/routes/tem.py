"""
通过模板渲染我们的视图
"""
from flask import render_template
from app.app import app


@app.route('/tem')
def tem():
    # 默认以/templates为根目录寻找模板
    return render_template('index.html',
                           title='flask tem',
                           user={'name': 'Jon'})
