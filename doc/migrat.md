# 1.安装

pip install Flask-Migrate

# 2.懒加载初始化

migrater = Migrate()

migrater.int_app(db,app)

# 3.manage.py中添加

manager.add_command('db',MigrateCommand)

# 4.数据迁移命令

```
$ python manager.py db init   ##创建数据表，并在根目录下添加migrations文件夹（保存数据库变更的记录） 

$ python manager.py db migrate  ##提交修改

$ python manager.py db upgrade  ##执行修改

$ python manager.py db downgrade  ##回退修改

```



