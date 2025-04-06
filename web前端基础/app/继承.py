from flask import Flask, request
from flask.views import View

class MyView(View):
    def __init__(self):
        self.methods = ['GET', 'POST']

    def dispatch_request(self, name):
        if request.method == 'GET':
            return f'Hello, {name}!'

app = Flask(__name__)
app.add_url_rule('/<name>', view_func=MyView.as_view('myview'))

if __name__ == '__main__':
    app.run(debug=True)
