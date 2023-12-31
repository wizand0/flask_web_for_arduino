import os
from app import app
from app.models import User, Todo, Sensors, db
# import app.admin


import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import BaseConfig

import config
#from app.handlers import router

FILENAME = "/data/todo.json" if "AMVERA" in os.environ else "todo.json"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    app.run(debug=False)

# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade


# if __name__ == '__main__':
#    with app.app_context():
#        db.create_all()
#        app.user_datastore.create_user(email='matt@nobien.net', password='password')
#    app.run()

# From Shell
# from app import db,app
# app.app_context().push()
# db.create_all()

# from cmd in the app's  folder:
# flask db init - This will add a migrations folder to your application. The contents of this folder need to be
# #added to version control along with your other source files.
# flask db migrate -m "Initial migration." - The migration script needs to be reviewed and edited, as Alembic is not
# #always able to detect every change you make to your models.
# flask db upgrade - Then you can apply the changes described by the migration script to your database

# git push amvera main:master

# https://cloud.amvera.ru/projects/flask-bot
# git push amvera dev:master --force
#
# Вам просто нужно правильно написать путь, но тут нет единого рецепта из-за возможных разных технологий, мы поэтому в
# документацию и не стали писать что-то конкретное, чтобы не путать.
# Обычно это выглядит как-то так \\\
# Просто нужно нужное количество слэшей указать.


# в login.html для ссылки на регистрацию добавить: <a href="{{url_for('register')}}">Регистрация</a>