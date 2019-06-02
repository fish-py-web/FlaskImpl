from flask import Flask
app = Flask(__name__)

"""
这里导入我们的路由函数，才能注册到我们的flask
"""
from app.routes.index import *
from app.routes.path import *
from app.routes.response import *
from app.routes.request import *
from app.routes.tem import *


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
