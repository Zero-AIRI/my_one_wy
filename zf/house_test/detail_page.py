from flask import Blueprint,render_template,jsonify
from models import House
from sqlalchemy import func

detail_page = Blueprint("detail_page",__name__)
@detail_page.route('/house/<int:hid>')
def detail(hid):
    house = House.query.get(hid)
    facilities_str = house.facilities
    facilities_list = facilities_str.split("-")
    return render_template("detail_page.html",house = house,facilities = facilities_list)
def deal_traffic_txt(word):
    if len(word) == 0 or word is None:
        return "暂无信息"
    else:
        return word
detail_page.add_app_template_filter(deal_traffic_txt,"dealNone")
@detail_page.route('/get/piedata/<block>')
def return_pie_data(block):
    result = House.query.with_entities(House.rooms,func.count()).\
        filter(House.block == block).group_by(House.rooms).\
        order_by(func.count().desc()).all()
    data = []
    for one_house in result:
        data.append({'name':one_house[0],'value':one_house[1]})
    return jsonify({'data':data})