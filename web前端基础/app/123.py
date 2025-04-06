from flask import Flask, render_template

app = Flask(__name__)

@app.route('/query-score/<int:score>')
def show_score(sccore):
    return render_template('sccore.html', score=sccore)  # 确保文件名没有空格

if __name__ == '__main__':
    app.run(debug=True)
