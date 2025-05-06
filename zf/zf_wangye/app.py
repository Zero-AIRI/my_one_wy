from flask import Flask, render_template
from settings import Config, db
from models import House
from index_page import index_page

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(index_page,url_prefix='/')
db.init_app(app)

# @app.route("/")
# def test():
#     first_user = House.query.get(18)
#     print(first_user)
#     return "OK"

if __name__ == "__main__":
    app.run(port=5001, debug=True)
