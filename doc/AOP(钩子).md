# AOP

​    面向切面编程
    在不修改原有胆码的情况下实现对逻辑的动态控制
    在django中叫做中间件
        -切点
            -哪个位置允许切入
        -切面 
            -切开后有哪些数据   
    在flask中称为"钩子"
        -黑语(外挂)
        -内置很多
            -蓝图
            -app
        -before_request
            @blue.before_request
            @blue.before_app_request
            @blue.before_app_first_request
        -errorhandler(401)
            -捕获401错误
            -蓝图中的只能捕获本蓝图的异常
            -app的可以处理全局
         -after_request
            -请求之后
         -terdown_request
            -关闭请求
    使用钩子可以实现的功能
        -日志统计
        -黑白名单
        -反爬
        -权限控制