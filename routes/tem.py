"""
通过模板渲染我们的视图
"""
from flask import render_template
from app import app


@app.route('/tem')
def tem():
    return render_template('index.html',
                           title='flask tem',
                           user={'name': 'Jon'})
