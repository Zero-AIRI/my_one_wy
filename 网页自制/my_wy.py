from flask import Flask, render_template
#   从flask里拿出两件工具 Flask(用来造网站的主工具)和render_template(用来显示网页的工具)直译为渲染模板

my_wy = Flask(__name__)
# 对本文件使用Flask类进行处理 并将其命名为my_wy

@my_wy.route("/")
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
    my_wy.run(port=5000, debug=True)
