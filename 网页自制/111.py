from flask import Flask, render_template
#   从flask里拿出两件工具 Flask(用来造网站的主工具)和render_template(用来显示网页的工具)直译为渲染模板

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/bg.html")  

@app.route("/school")
def about():
    return render_template("school.html")

if __name__ == "__main__":
    app.run(debug=True)
