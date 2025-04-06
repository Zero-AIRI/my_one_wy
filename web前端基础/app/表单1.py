from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST'])

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
   

@app.route('/')
def home():
    return render_template('表单1.html')

if __name__ == '__main__':
       app.run()