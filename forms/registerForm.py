from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()], render_kw={"placeholder": "Фамилия"})
    name = StringField('Имя', validators=[DataRequired()], render_kw={"placeholder": "Имя"})
    email = EmailField('Почта', validators=[DataRequired()], render_kw={"placeholder": "Почта"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    password_confirmation = PasswordField('Пароль', validators=[DataRequired()],
                                          render_kw={"placeholder": "Повторите пароль"})
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')
