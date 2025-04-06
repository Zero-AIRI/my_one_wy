from flask.views import MethodView
from flask import Flask, render_template, request

class LoginView(MethodView):
    def get(self):
        return render_template('表单3.html')  # 处理GET请求

    def post(self):
        username = request.form.get('username')  # 获取输入的用户名
        password = request.form.get('password')  # 获取输入的密码
        # 判断用户名和密码是否为123
        if username == 'hhp' and password == '123':
            return f'用户：{username} 登录成功。'
        else:
            return '用户名或密码错误，请重新登录。'

app = Flask(__name__)
app.add_url_rule('/', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run(debug=True)
