import os

# 配置 static路径和templates路径,App/__init_中调用
import redis

BASEDIR = os.getcwd();

STATICPATH = os.path.join(BASEDIR, "App/static")

TEMPLATESPATH = os.path.join(BASEDIR, "App/static/html")

# 配置数据库的链接信息
DATABASE = {
    "ENGIN": 'mysql',

    "DRIVER": "pymysql",

    "USER": os.getenv("DB_USER"),

    "PASSWORD": os.getenv("DB_PWD"),

    "DOMAIN": "127.0.0.1",

    "PORT": "3306",

    "NAME": "db_cement_bill"
}


def get_database_uri(database):
    '''
    生成链接数据库的URI
    :param database:
    :return: 链接数据库的URI
    '''
    engin = database.get("ENGIN")

    driver = database.get("DRIVER")

    user = database.get("USER")

    password = database.get("PASSWORD")

    domain = database.get("DOMAIN")

    port = database.get("PORT")

    name = database.get("NAME")

    ##数据库名+数据库驱动://username:password@url:port/databaseName
    return "{}+{}://{}:{}@{}:{}/{}".format(engin, driver, user, password, domain, port, name)


class BasicConfig:

    DEBUG = False

    # 使用session的时候必须要添加密钥
    #生成方式:os.urandom(24)
    SECRET_KEY = b'\xbb\x1aSQ\x94O\xa9\xce6\xd4\x19\xf6\xbe\xdb\xc08\xdc\x04\x00\xaf\xa5\x99-\xe1'


class DevelopConfig(BasicConfig):

    DEBUG = True

    #设置会话路徑,即决定哪些路由下应该设置cookies；默认"/",所有路由下都会设置cookie
    SESSION_COOKIE_PATH = '/'

    #为cookie设置签名来保护数据不被更改
    # SESSION_USE_SIGNER = True

    #设置session的存储信息
    # 指明保存到redis中
    SESSION_TYPE = "redis"

    # redis.StrictRedis(host="127.0.0.1", port=6390, db=4)
    SESSION_REDIS = redis.StrictRedis()

    #设置session的有效期(单位：S)
    PERMANENT_SESSION_LIFETIME = 30

    # SQLAlchemy配置
    SQLALCHEMY_DATABASE_URI = get_database_uri(DATABASE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 加载配置环境,目前就设置了开发环境配置
ENV = {
    "development": DevelopConfig,

    "default": DevelopConfig,

    "test": None,

    "product":None
}
