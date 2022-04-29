from flask import Blueprint, render_template, jsonify, redirect, url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask_login import login_required

crud = Blueprint('crud',__name__,template_folder='templates')

@crud.route('/')
@login_required
def index():
    return render_template('crud/index.html')

@crud.route('/users/new', methods=['POST','GET'])
@login_required
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('crud.users'))
    return render_template('crud/create.html', form=form)

@crud.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('crud/index.html', users=users)

@crud.route('/users/<user_id>', methods=['POST','GET'])
@login_required
def edit_user(user_id):
    form = UserForm()
    user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))
    return render_template('crud/edit.html', user=user, form=form)

@crud.route('users/<user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('crud.users'))

@crud.route('/sql')
@login_required
def sql():
    # 基本的検索
    # res = db.session.query(User).all()
    # db.session.query(User).first()
    # db.session.query(User).first_or_404()
    # db.session.query(User).get(0)
    # db.session.query(User).count()
    # db.session.query(User).paginate(2,10,False)
    # db.session.query(User).filter_by(id=2, username='admin').all()
    # db.session.query(User).filter(User.id==2, User.username=='admin').all()
    # db.session.query(User).limit(1).all()
    # db.session.query(User).limit(1).offset(2).all()
    # db.session.query(User).order_by('username').all()
    # db.session.query(User).group_by('username').all()

    # データをinsertする
    # user = User(username='kohama23', email='apollo23@gmail.com', password='123123')
    # db.session.add(user)
    # db.session.commit()

    # データを更新する
    # user = db.session.query(User).filter_by(id=1).first()
    # user.username = 'hisae'
    # user.email = '123@gmail.com'
    # db.session.add(user)
    # db.session.commit()

    # データを削除する
    # user = db.session.query(User).filter_by(id=1).delete()
    # db.session.commit()

    return jsonify({'data':'success'})