from flask import render_template

from index import index_blue
from app import db, Info, Focus


@index_blue.route('/')
def index():
    info = Info.query.all()
    return render_template('index.html', info=info)


@index_blue.route('/<code_id>')
def add_focus(code_id):
    info = Info.query.all()
    stock = Info.query.filter(Info.code == code_id).first()

    # 判断是否存在股票，不存在提示非法请求
    if stock:
        stock_id = stock.id
        print(stock_id)

        get_focus = Focus.query.filter(Focus.info_id==stock_id).first()

        # 判断是否关注过，关注过提示已经关注
        if not get_focus:
            new_focus = Focus(note_info='', info_id=stock_id)
            db.session.add(new_focus)
            db.session.commit()

            alert = "<script>alert('%s add Successful')</script>" % code_id

        else:
            alert = "<script>alert('%s already existed')</script>" % code_id

    else:
        alert = "<script>alert('access denied')</script>"

    return render_template('index.html',
                           info=info,
                           alert=alert)
