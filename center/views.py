from flask import render_template, redirect, url_for

from center import center_blue
from app import db, Info, Focus


@center_blue.route('/')
def center():
    info = Info.query.filter(Info.id == Focus.info_id).all()

    # test = Info.query.filter(Info.id == Focus.info_id).first()
    # print(info[1].focus[0].note_info)
    # info[1].focus
    # info[1].focus.all()
    # print(test.focus[0])

    return render_template('center.html', info=info)


@center_blue.route('/<code_id>')
def del_focus(code_id):
    info = Info.query.filter(Info.id == Focus.info_id).all()
    stock = Info.query.filter(Info.code == code_id).first()

    if stock:
        stock_id = stock.id
        focus = Focus.query.filter(Focus.info_id == stock_id).first()

        # 判断是否关注过，未关注过，提示还未关注
        if focus:
            db.session.delete(focus)
            db.session.commit()
            # alert = "<script>alert('%s delete Successful')</script>" % code_id
    
        else:
            alert = "<script>alert('%s hasn't been focused')</script>" % code_id
            return render_template('center.html',
                                   info=info,
                                   alert=alert)

    return redirect(url_for('center.center'))