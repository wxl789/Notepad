from flask import Flask

from App import settings

from App.exp import init_exp

from App.settings import ENV

from App.views import init_views


def create_app(config):
    app = Flask(__name__, template_folder=settings.TEMPLATESPATH, static_folder=settings.STATICPATH)

    # 加载app配置文件
    app.config.from_object(ENV.get(config))

    # 初始化蓝图
    init_views(app)

    # 初始化插件
    init_exp(app)

    return app
