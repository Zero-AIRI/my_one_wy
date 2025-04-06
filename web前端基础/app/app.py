from flask import Flask, render_template

app = Flask(__name__)

@app.route('/query-score/<int:score>')
def query_score(score):
    return render_template('2025311.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
