from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user

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


@login_manager.request_loader
def request_loader(request):
    '''
    请求加载回调函数
    :return:
    '''
    name = request.form.get('username')

    try:
        user = User.query.filter(User.username == name).first()
    except:
        return None

    # DO NOT ever store passwords in plaintext and always compare password
    # 这里应该使用hansh进行密码验证
    if user:
        user.is_authenticated = request.form.get('password') == user.password

    return user


@bp.route('/')
@bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')

    name = request.form.get('username')

    try:
        user = User.query.filter(User.username == name).first()

        if user.password == request.form.get('password'):
            login_user(user, remember=True, fresh=False)

            return redirect(url_for("indexBP.index"))
        else:
            '''
                需要添加错误提示
            '''
            flash("用户名或者密码错误")
            return ""

    except:
        flash("用户名或者密码错误")

        return ""


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
    flash ("需要登录验证才能访问")
    return redirect(url_for("loginBP.login"))

