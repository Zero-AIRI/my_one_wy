from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # 必须添加：用于 CSRF 保护

class RegisterForm(FlaskForm):
    username = StringField(label='用户名：',
                           validators=[DataRequired(message='用户名不能为空'),
                                       Length(3, 15, message='长度应为3~15')])
    password = PasswordField('密码：',
                             validators=[DataRequired(message='密码不能为空')])
    password2 = PasswordField('确认密码：',
                              validators=[DataRequired(message='密码不能为空'),
                                          EqualTo('password', message='两次密码不一致')])
    submit = SubmitField('注册')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        # 此处可添加数据库操作（如保存用户名和密码）
        return "注册成功！"
    return render_template('表单1.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)  # 添加 debug=True 便于调试
