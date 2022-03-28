from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length, ValidationError

class UserForm(FlaskForm):
    username = StringField('ユーザー名', validators=[
        DataRequired(message='ユーザー名は必須です'),
        length(max=30, message='30文字以内で入力ください'),
    ])
    email = StringField('メールアドレス', validators=[
        DataRequired(message='メールアドレスは必須です'),
        Email(message='メールアドレスの形式で入力してください'),
    ])
    password = PasswordField('パスワード', validators=[
        DataRequired(message='パスワードは必須です'),
    ])
    submit = SubmitField('新規登録')

    # Customized validator
    # メソッド名: validate_フィールド名
    # エラー時はraise ValidationErrorを発生させる
    # def validate_username(self, username):
    #     if not username.data:
    #         raise ValidationError('ユーザー名は必須です')