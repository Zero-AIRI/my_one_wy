from flask import Flask, render_template

app = Flask(__name__)


@app.route('/yuanshen')
def goods():
    goods_name = ['派蒙', '派蒙', '派蒙', '派蒙', '派蒙']
    return render_template('物品.html', goods_name=goods_name)

if __name__ == '__main__':
    app.run(debug=True)
