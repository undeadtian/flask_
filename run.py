# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 下午5:12
# @Author  : wth
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from .models import *

app = Flask(__name__, static_url_path='/', static_folder='./../../flask-dist', template_folder='./../../flask-dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wth:123456@127.0.0.0:3306/mls_web'
# mysql+pymysql 这是声明数据库和链接数据库的引擎  name pwd 就是可以访问数据库的用户名密码 106.13.174.205:3306 是数据库地址 /mls_web 这是数据库名字

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_UCSO'] = True
# 声明数据对象
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getUser', methods=['GET', 'POST'])   # 查询数据的接口
def get_user():
    res = db.session.query(User).all()				#User是从models里导入的
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(data=temp)


@app.route('/addUser', methods=['POST'])      #新增数据的接口
def add_user():
    data = request.json        #获取传过来的参数
    u = User(name=data.get("name"),pwd=data.get("pwd"))      #根据传过来参数创建一条数据
    db.session.add(u)  #add 是增加数据
    db.session.commit()   #提交了才会到数据库中
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)

