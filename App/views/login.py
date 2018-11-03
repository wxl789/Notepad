from flask import Blueprint, request, render_template, redirect, url_for, flash, json
from flask.json import jsonify
from flask_login import login_user, logout_user, current_user

from App.exp import login_manager
from App.models.user_model import User

bp = Blueprint('loginBP', __name__)


@login_manager.user_loader
def loader_user(id):
    '''
    用户加载回调函数
    :param id:
    :return:
    '''

    try:
        user = User.query.get(id)
    except:
        user = None

    return user


@bp.route('/')
@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if( current_user.is_authenticated):
            return redirect(url_for("indexBP.index"))

        return render_template('login.html')

    try:
        results = request.get_data()

        results = json.loads(results)

        datas = results.get("data")
    except:
        return jsonify({
            "code": 0,
            "msg": "数据不是json标准格式,或入参没有data关键字",
            "data": "",
        })

    name = datas.get("username")
    pwd = datas.get("password")


    try:
        user = User.query.filter(User.username == name).first()

        if user.verify_password(pwd):
            login_user(user, remember=True, fresh=False)

            res = {
                "code": 1,
                "msg": "登录成功",
                "data": "/index",
            }
        else:
            res = {
                "code": 0,
                "msg": "用户名或者密码错误",
                "data": "",
            }

    except:
        res = {
            "code": 0,
            "msg": "用户名或者密码错误",
            "data": "",
        }

    return jsonify(res)


@bp.route('/logout/')
def logout():
    '''
    用户登出请求函数
    :return:
    '''
    logout_user()

    return redirect(url_for("loginBP.login"))


@login_manager.unauthorized_handler
def unauthorized_handler():
    '''
        未登录就访问login_required修饰的路由则会调用此函数
    :return:
    '''
    return redirect(url_for("loginBP.login"))


@bp.route("/update_pwd/",methods = ["GET","POST"])
def update_password():
    '''

    :return:
    '''
    try:
        results = request.get_data()

        results = json.loads(results)

        datas = results.get("data")
    except:
        return jsonify({
            "code": 0,
            "msg": "数据不是json标准格式,或入参没有data关键字",
            "data": "",
        })

    oldpwd = datas.get("oldpassword")
    newpwd = datas.get("newpassword")
    confirmpwd = datas.get("confirmpassword")

    if current_user.verify_password(oldpwd):

        if newpwd == confirmpwd:

            current_user.password = newpwd

            res = {
                "code":1,
                "msg":"密码更新成功,请重新登录",
                "data":"/logout/",
            }
        else:
            res = {
                "code":2,
                "msg":"新密码两次输入不相同",
                "data":"",
            }

    else:
        res = {
            "code":0,
            "msg":"用户密码输入错误",
            "data":"",
        }

    return jsonify(res)


@bp.route("/getuser/")
def get_current_username():
    res = {
        "code": 1,
        "msg": "",
        "data": current_user.username,
    }

    return jsonify(res)

