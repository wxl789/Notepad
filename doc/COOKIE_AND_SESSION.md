# cookie和session机制

## cookie

### 机制

​    cookie实际上是一小段文本信息,当客户端请求服务器时,如果服务器需要记录该用户状态,就是用response向浏览器颁发一个cookie,客户端浏览器会把cookie保存起来.
    当浏览器再次向该网站请求时,就会携带cookie下发,服务器就可以通过检验cookie来确认身份.
    

### **特性**:
    -客户端会话技术<br>
    
    -数据都存储在浏览器中<br>
    
    -支持过期<br>
    
    -不能跨域名<br>
    
    -不能跨浏览器<br>
    
    -cookie是通过response来进行操作的

### cookie的使用:

```
1.导入make_response包和request包
from flask import make_response,request

2.创建响应
resp = make_response(render_template("index.html"))
or
resp = redirect(url_for("indexBP.to_index"))

3.设置cookie并返回给浏览器
resp.set_cookie("user",value=username)
return resp

4.获取cookie
request.cookies.get("user")

5.删除cookie

resp.delete_cookie('user')
return resp

```

## session

### 机制

​    是服务器端使用的一种记录客户端状态的机制,数据存放在server端,客户端再次访问的时候只需要从session中找到该客户的状态就可以了.

### **特性:**

1.server端会话技术

2.对数据进行数据安全操作

3.默认在内存中
    
    -不易管理
    
    -容易丢失
    
    -不能多台电脑协作

4.flask-session 默认有效期31天

### session在flask中的配置

```
    #设置会话路徑,即决定哪些路由下应该设置cookies；默认"/",所有路由下都会设置cookie
    SESSION_COOKIE_PATH = '/'

    #为cookie设置签名来保护数据不被更改
    SESSION_USE_SIGNER = True

    #设置session的存储信息
    # 指明保存到redis中
    SESSION_TYPE = "redis"

    # redis.StrictRedis(host="127.0.0.1", port=6390, db=4)
    SESSION_REDIS = redis.StrictRedis()
        
    #设置session的有效期(单位：S)
    PERMANENT_SESSION_LIFETIME = 30
```





### session的使用:

```
login.py中使用了session技术:

1.导入session包:

from flask import session

2.设置secret_key

在app初始化的时候设置

app.secret_key = b'\xbb\x1aSQ\x94O\xa9\xce6\xd4\x19\xf6\xbe\xdb\xc08\xdc\x04\x00\xaf\xa5\x99-\xe1'

这个secret_key可以通过os.urandom(24)生成一个强壮的随机值

2.添加session value

session["username"] = username

3.获取session  value

session.get("username")

4.flask-session 插件 -- 将数据存储在redis中

    -添加配置:    app.config["SESSION_TYPE"] = "redis"
    
    -初始化插件:   Session(app)  
    
    -启动redis-server
    
    -打开页面登录,查看cookie中session的key
    
    -查看redis中session的value
    
        启动客户端:redis-cli
        
        查看所有的key: key *
        
        获取key对应的value:get key
        
```

