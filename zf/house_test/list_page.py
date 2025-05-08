from flask import Blueprint,request,render_template
from models import House
import math
list_page = Blueprint("list_page",__name__)
@list_page.route("/query")
def search_txt_info():
    if request.args.get("addr"):
        addr = request.args.get("addr")
        result = House.query.filter(House.address==
                                    addr).order_by(House.publish_time.desc()).all()
        return render_template("search_list.html",house_list = result)
    if request.args.get("rooms"):
        rooms_info = request.args.get("rooms")
        result = House.query.filter(House.address==
                                    rooms_info).order_by(House.publish_time.desc()).all()
        return render_template("search_list.html",house_list = result)

@list_page.route('/list/pattern/<int:page>')
def return_new_list(page):
    house_num = House.query.count()
    total_num = math.ceil(house_num/10)
    result = House.query.order_by(House.publish_time.desc()).paginate(page = page,per_page = 10,error_out=False)
    return render_template('list.html',house_list = result.items,page_num = result.page,total_num = total_num)
@list_page.route('/list/hot_house/<int:page>')
def return_hot_list(page):
    # 获取房源总数量
    house_num = House.query.count()
    # 计算总的页码数，向上取整
    total_num = math.ceil(house_num / 10)
    result = House.query.order_by(
        House.page_views.desc()).paginate(page = page,per_page = 10,error_out=False)
    return render_template('list.html', house_list=result.items, page_num=result.page, total_num=total_num)

def deal_title_over(word):
    if len(word) > 15:
        return word[:15] + '...'  # 当房源标题长度大于15时，用省略号替换
    else:
        return word

def deal_direction(word):
    if len(word) == 0 or word is None:  # 房源朝向、交通条件为空时显示暂无信息
        return '暂无信息！'
    else:
        return word
list_page.add_app_template_filter(deal_title_over, 'dealover')
list_page.add_app_template_filter(deal_direction, 'dealdirection')