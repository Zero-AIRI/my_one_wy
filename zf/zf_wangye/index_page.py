from flask import Blueprint, render_template,request
from models import House

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    house_total_num = House.query.count()
    
    house_new_list = House.query.order_by(House.publish_time.desc()).limit(6).all()
    house_hot_list = House.query.order_by(House.page_views.desc()).limit(4).all()
    
    return render_template("index.html", num=house_total_num,
                           house_new_list=house_new_list,
                           house_hot_list=house_hot_list)

