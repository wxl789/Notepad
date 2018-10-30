from App.views.cement_view import bp as cement_bp
from App.views.index import bp as index_bp
from App.views.login import bp as login_bp


def init_views(app):
    '''
    注册各个views的蓝图
    :param app:在app创建后进行初始化时传入Flask对象(app)
    :return: None
    '''
    app.register_blueprint(blueprint=login_bp)
    app.register_blueprint(blueprint=index_bp)
    app.register_blueprint(blueprint=cement_bp)

    return None