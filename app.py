from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, supports_credentials=True)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123aaa@localhost:3306/guo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zjb1234.@localhost:3306/guo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(255))
    product_name = db.Column(db.String(255))
    product_desc = db.Column(db.String(255))
    old_price = db.Column(db.String(255))
    price = db.Column(db.String(255))
    volume = db.Column(db.String(255))
    warehouse = db.Column(db.String(255))
    catalog = db.Column(db.String(255))
    origin = db.Column(db.String(255))
    sales = db.Column(db.String(255))

    def to_json(self):
        json_product = {
            'id': self.id,
            'photo': self.photo,
            'product_name': self.product_name,
            'product_desc': self.product_desc,
            "old_price": self.old_price,
            "price": self.price,
            "volume": self.volume,
            "warehouse": self.warehouse,
            "catalog": self.catalog,
            "origin": self.origin,
            "sales": self.sales
        }
        return json_product


def enum(hotList):
    result = []
    for hot in hotList:
        result.append(hot.to_json())
    return jsonify(result)


@app.route('/recList')
def products():
    return enum(product.query.filter_by(catalog='rec'))


@app.route('/hotList')
def hotList():
    return enum(product.query.filter_by(catalog='hot'))


@app.route('/giftList')
def giftList():
    return enum(product.query.filter_by(catalog='gift'))


# if __name__ == '__main__':
# #     app.run()
