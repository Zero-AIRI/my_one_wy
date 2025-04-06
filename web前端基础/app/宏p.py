
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('静态图片.html')

@app.route('/aab')
def homea():
    return render_template('c.html')



if __name__ == '__main__':
    app.run(debug=True)
    