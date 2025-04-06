from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = '556666'

@app.route('/', methods=['GET', 'POST'])
def register():
    # 判断请求方式
    if request.method == 'POST':
        # 获取表单数据
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 验证表格的完整性
        if not all([username, password, password2]):
            flash('请填入完整信息', category='message')

        # 验证输入的数据是否符合要求
        elif len(username) < 3 or len(username) > 15:
            flash('用户名长度大于3且小于15', category='info')
        
        # 验证两次输入的密码是否一致
        elif password != password2:
            flash('密码不一致', category='error')
        
        else:
            return "注册成功"

    return render_template('表单.html')

if __name__ == '__main__':
    app.run()
