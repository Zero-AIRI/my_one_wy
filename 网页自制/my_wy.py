from flask import Flask, render_template
#   从flask里拿出两件工具 Flask(用来造网站的主工具)和render_template(用来显示网页的工具)直译为渲染模板

my_wy = Flask(__name__)
# 对本文件使用Flask类进行处理 并将其命名为my_wy  在Python里是一个特殊变量，它代表“当前这个文件的名字”。

@my_wy.route("/")
# 路由（Route）的核心作用，就是决定“当用户访问某个特定地址（URL）时，哪个函数应该被触发执行”。
def zhuye():
    return render_template("/bg.html")  

@my_wy.route("/school")
def school():
    return render_template("school.html")

@my_wy.route("/what")
def what():
    return render_template("what.html")

@my_wy.route("/world")
def world():
    return render_template("world.html")


if __name__ == "__main__":
    my_wy.run(port=520, debug=True)
