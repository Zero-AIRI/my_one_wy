from settings import db

class House(db.Model):
    __tablename__ = 'house_info'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    rooms = db.Column(db.String(100))
    area = db.Column(db.String(100))
    price = db.Column(db.String(100))
    direction = db.Column(db.String(100))
    rent_type = db.Column(db.String(100))
    region = db.Column(db.String(100))
    block = db.Column(db.String(100))
    address = db.Column(db.String(200))
    traffic = db.Column(db.String(100))
    publish_time = db.Column(db.Integer)
    facilities = db.Column(db.Text)
    highlights = db.Column(db.Text)
    matching = db.Column(db.Text)
    travel = db.Column(db.Text)
    page_views = db.Column(db.Integer)
    landlord = db.Column(db.String(30))
    phone_num = db.Column(db.String(100))
    house_num = db.Column(db.String(100))

    def __repr__(self):
        return f"<House {self.title}>"
    
class House_recommend(db.Model):
    __tablename__ = 'house_recommend'  # 数据库表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 关联用户表
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))  # 关联房屋表
    title = db.Column(db.String(100))
    address = db.Column(db.String(100))
    block = db.Column(db.String(100))
    score = db.Column(db.Integer)

class user_info(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    addr = db.Column(db.String(100))
    collect_id = db.Column(db.String(250))  # 存储用户收藏的房屋ID列表
    seen_id = db.Column(db.String(250))  # 存储用户浏览过的房屋ID列表  