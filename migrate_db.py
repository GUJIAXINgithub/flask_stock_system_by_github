from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库连接属性
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:429005@localhost:3306/stock_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化数据库对象
db = SQLAlchemy(app)

# 创建终端命令的对象
manger = Manager(app)
# 1.使用迁移类将应用对象app和数据库对象保存起来
Migrate(app, db)
# 2.将数据库迁移的命令添加到manger中
manger.add_command('db', MigrateCommand)

# 建立数据表模型
"""
info
+----------+------------------+------+-----+---------+----------------+
| Field    | Type             | Null | Key | Default | Extra          |
+----------+------------------+------+-----+---------+----------------+
| id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| code     | varchar(6)       | NO   |     | NULL    |                |
| short    | varchar(10)      | NO   |     | NULL    |                |
| chg      | varchar(10)      | NO   |     | NULL    |                |
| turnover | varchar(255)     | NO   |     | NULL    |                |
| price    | decimal(10,2)    | NO   |     | NULL    |                |
| highs    | decimal(10,2)    | NO   |     | NULL    |                |
| time     | date             | YES  |     | NULL    |                |
+----------+------------------+------+-----+---------+----------------+
"""


class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    code = db.Column(db.String(6), nullable=False)
    short = db.Column(db.String(10), nullable=False)
    chg = db.Column(db.String(10), nullable=False)
    turnover = db.Column(db.String(255), nullable=False)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    highs = db.Column(db.DECIMAL(10, 2), nullable=False)
    time = db.Column(db.DATE, nullable=False)

    focus = db.relationship('Focus',
                            backref=db.backref('info', lazy='dynamic'),
                            lazy='dynamic')


"""
focus
+-----------+------------------+------+-----+---------+----------------+
| Field     | Type             | Null | Key | Default | Extra          |
+-----------+------------------+------+-----+---------+----------------+
| id        | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| note_info | varchar(200)     | YES  |     |         |                |
| info_id   | int(10) unsigned | YES  | MUL | NULL    |                |
+-----------+------------------+------+-----+---------+----------------+
"""


class Focus(db.Model):
    __tablename__ = 'focus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    note_info = db.Column(db.String(200))
    info_id = db.Column(db.Integer, db.ForeignKey(Info.id))


if __name__ == '__main__':
    manger.run()
