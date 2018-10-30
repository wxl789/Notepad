# 1.运行app之前开启必要的server

    redis-server          --存储session缓存
    service mysqld start  --启动数据库保证数据库服务

# 2.启动app

    python manager runserver -h 0.0.0.0 -p 5000 -d -r 