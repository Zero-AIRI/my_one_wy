from flask import Flask, render_template
from settings import Config, db
from models import House

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def test():
    first_user = House.query.get(18)
    print(first_user)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
