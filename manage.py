# -*-coding:utf-8 -*-
import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

# 从系统中获取环境变量,如果没有返回"default"
app = create_app(os.getenv("FLASK_ENV") or "default")

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
