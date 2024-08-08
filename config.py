import os
basedir = os.path.abspath(os.path.dirname(__file__))
# URI – https://wiki.merionet.ru/images/vse-chto-vam-nuzhno-znat-pro-devops/1.png
# URL - https://wiki.merionet.ru
# URN - images/vse-chto-vam-nuzhno-znat-pro-devops/1.png
class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "12345"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")