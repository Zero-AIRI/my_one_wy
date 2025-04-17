from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/bg.html")  # 需自行创建

@app.route("/school")
def about():
    return render_template("school.html")

if __name__ == "__main__":
    app.run(debug=True)
