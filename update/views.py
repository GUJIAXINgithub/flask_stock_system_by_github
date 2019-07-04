from flask import render_template, request, redirect, url_for

from update import update_blue
from app import db, Info, Focus


# /update/000007[?info=xxx]
@update_blue.route('/<code_id>')
def update(code_id):
    info = Info.query.filter(Info.id == Focus.info_id).all()
    stock = Info.query.filter(Info.code == code_id).first()
    # 判断是否存在这只股票
    if stock:
        focus = Focus.query.filter(Focus.info_id == stock.id).first()

        # 判断这只股票是否关注过
        if focus:
            # 获取数据库中的备注信息
            focus_info = focus.note_info

            flag = ('null')

            # 获取url参数
            new_info = request.args.get('info', flag)

            if new_info==flag:
                # 说明url中没有参数，是从center点击‘修改’进来的，直接渲染update.html
                print('1')
                return render_template('update.html',
                                       code_id=code_id,
                                       focus_info=focus_info)
            else:
                # 说明有参数info='xxx'，js中有判断，不修改不能提交，所以说明肯定修改了内容
                focus.note_info = new_info
                db.session.commit()
                print('2')
                return redirect(url_for('center.center'))


        else:
            alert = "<script>alert('%s hasn't been focused')</script>" % code_id
            return render_template('center.html',
                                   info=info,
                                   alert=alert)
    else:
        alert = "<script>alert('access denied')</script>"
        return render_template('center.html',
                               info=info,
                               alert=alert)