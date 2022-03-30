from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
# login_view属性に未ログイン時にredirectするendpointを指定する
login_manager.login_view = 'auth.signup'
# login_message属性にログイン後に表示するメッセージを指定する、なにもない場合、空を指定する
login_manager.login_message = ''

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='salkjrwoijxlkv',
        SQLALCHEMY_DATABASE_URI=f"sqlite:////{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # コンソールログに出力する設定
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY='alsdkjqlekjr',
    )
    db.init_app(app)
    Migrate(app,db)
    csrf.init_app(app)
    login_manager.init_app(app)

    # ログインしているユーザー情報を取得する関数を作成する
    @login_manager.user_loader
    def load_user(user_id):
        from apps.crud.models import User
        return User.query.get(user_id)

    from apps.crud import views as crud_views
    from apps.auth import views as auth_views

    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    app.register_blueprint(auth_views.auth, url_prefix='/auth')

    return app

