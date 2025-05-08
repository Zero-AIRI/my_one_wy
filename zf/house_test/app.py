from flask import Flask,render_template
from settings import Config,db
from models import House
from index_page import index_page
from list_page import list_page
from detail_page import detail_page
app = Flask(__name__)
app.register_blueprint(index_page,url_prefix = "/")
app.register_blueprint(list_page,url_prefix = "/")
app.register_blueprint(detail_page,url_prefix = "/")
app.config.from_object(Config)
db.init_app(app)
# @app.route('/')
# def test():  # put application's code here
#     #return render_template("index.html")
#     first_user = House.query.first()
#     print(first_user)
#     return "OK"

if __name__ == '__main__':
    app.run(debug=True,port=5001)
