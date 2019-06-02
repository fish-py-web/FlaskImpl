from flask import Flask
app = Flask(__name__)

"""
这里导入我们的路由函数，才能注册到我们的flask
"""
from routes.index import hello_world
from routes.tem import tem
from routes.path import path

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
