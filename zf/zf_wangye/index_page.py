from flask import Blueprint, render_template, request, jsonify
from models import House
from sqlalchemy import func

index_page = Blueprint("index_page", __name__)

@index_page.route("/")
def index():
    house_total_num = House.query.count()
    house_new_list = House.query.order_by(House.publish_time.desc()).limit(6).all()
    house_hot_list = House.query.order_by(House.page_views.desc()).limit(4).all()
    
    return render_template("index.html", 
                         num=house_total_num,
                         house_new_list=house_new_list,
                         house_hot_list=house_hot_list)

@index_page.route("/search/keywords", methods=['POST'])
def search_kw():
    kw = request.form['kw']
    info = request.form['info']  # 获取用户选择的搜索选项

    if info == '地区搜索':
        house_data = House.query.with_entities(
            House.address, func.count()
        ).filter(House.address.contains(kw))
        
        result = house_data.group_by('address').order_by(
            func.count().desc()).limit(9).all()

    elif info == '户型搜索':
        house_data = House.query.with_entities(
            House.rooms, func.count()
        ).filter(House.rooms.contains(kw))

        result = house_data.group_by('rooms').order_by(
            func.count().desc()).limit(9).all()

    if len(result):  # 有查询结果
        data = []
        for i in result:
            # 将查询的房源数据添加到列表中
            data.append({'t_name': i[0], 'num': i[1]})
        return jsonify({'code': 1, 'info': data})
    else:  # 没有查询结果
        return jsonify({'code': 0, 'info': []})
    
