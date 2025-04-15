from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text,column

app = Flask(__name__)

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'flask'

# 组装数据库的连接信息
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 测试连接到数据库
with app.app_context():
    with db.engine.connect() as conn:
        res = conn.execute(text('SELECT 1'))
        print(res.fetchone())

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
# with app.app_context():
#     db.create_all()

# db.drop_all() # 添加数据
# @app.route("/")
# def add_user():
#     # 创建对象
#     user1 = User(username="小明", password="123456")
#     user2 = User(username="小红", password="678910")
#     user3 = User(username="小强", password="abcdefgh")
#     # 将对象添加到数据库会话
#     db.session.add(user2)
#     db.session.add_all([user1, user2, user3])
#     # 使用commit()方法从会话提交至数据库
#     db.session.commit()
#     return "用户创建成功!"

# if __name__ == '__main__':
#     app.run()

# # 查询数据
# @app.route("/")
# def query_user():
#     # get查找后键，只能找到一条数据
#     user = User.query.get(1)
#     print(f"{user.id}:{user.username}---{user.password}")
    
#     # filter by查找
#     users = User.query.filter_by(username="小明")
#     print(type(user))
#     for user in users:
#         print(user.username)
    
#     return "数据查询成功"


# @app.route("/")
# def update_user():
#     user = User.query.filter_by(username="小明").first()  # 查询名为“小明”的用户
#     user.password = "213"  # 更新用户的密码
#     db.session.commit()  # 提交更改到数据库
#     db.session.refresh(user)
#     return "更新修改数据成功"

# if __name__ == '__main__':
#     with app.app_context():  # 确保在应用上下文中运行
#         user = User.query.filter_by(username="小红").first()
#         if user:
#             user.password = "我是我爸"
#             db.session.commit()
#             print("数据库修改成功！")
#         else:
#             print("用户不存在")
            

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 添加作者外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # backref: 会自动给User模型添加articles的属性, 用来获取文章列表
    author = db.relationship("User", backref="articles")

with app.app_context():
    db.create_all()
    # db.drop_all()


@app.route("/")
def article_add():
    article1 = Article(title="数据服务", content="数据服务课程内容")
    article1.author = User.query.get(1)
    article2 = Article(title="python web课程", content="python web课程内容")
    article2.author = User.query.get(2)
    db.session.add_all([article1, article2])
    db.session.commit()
    return "文章添加成功！"

if __name__ == '__main__':
    app.run()