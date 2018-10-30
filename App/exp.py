import flask_excel as excel

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemy插件
# Flask_Migrate 插件

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()


def init_exp(app):
    '''
    初始化外部扩展插件
    :param app: 在app创建后进行初始化时传入Flask对象(app)
    :return: None
    '''

    # flask-session插件
    Session(app=app)

    # flask-SQLAlchemy插件初始化
    db.init_app(app=app)

    #flask-migrate插件初始化
    migrate.init_app(app=app, db=db)

    #flask-excel插件
    excel.init_excel(app)

    #flask-login 插件初始化.
    # login_manager.session_protection = "strong"
    # login_manager.login_view = "loginBP.login"
    # login_manager.login_message = "请登录"
    login_manager.init_app(app=app)

    return None
