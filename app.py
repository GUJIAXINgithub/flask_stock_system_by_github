from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库连接属性
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:429005@localhost:3306/stock_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化数据库对象
db = SQLAlchemy(app)


# 建立表模型
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
                            backref='info',
                            lazy='dynamic')


class Focus(db.Model):
    __tablename__ = 'focus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    note_info = db.Column(db.String(200))
    info_id = db.Column(db.Integer, db.ForeignKey(Info.id))


@app.route('/')
def login():
    return render_template('login.html')


from index import index_blue
from center import center_blue
from update import update_blue

app.register_blueprint(index_blue)
app.register_blueprint(center_blue)
app.register_blueprint(update_blue)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
