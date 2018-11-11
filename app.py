from flask import Flask, jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from urllib import parse

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zjb1234.@47.99.44.43:3306/guo'
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
    spec = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    pack = db.Column(db.String(255))
    period = db.Column(db.String(255))
    storage = db.Column(db.String(255))
    activity = db.Column(db.String(255))
    scan = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False)

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
            "sales": self.sales,
            "spec":self.spec,
            "weight":self.spec,
            "pack":self.pack,
            "period":self.period,
            "storage":self.storage,
            "activity":self.activity,
            "scan":self.scan,
            "create_time":self.create_time
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


@app.route('/productDetail')
def productDetail():
    productid = request.values.get("productid")
    return enum(product.query.filter_by(id=productid))


@app.route('/productList')
def productList():
    if parse.unquote(request.values.get("productname"))=="undefined":
        productname = ""
    else:
        productname = parse.unquote(request.values.get("productname")) or ""
    return enum(product.query.filter(product.product_name.like('%'+str(productname)+'%')))


# if __name__ == '__main__':
#     app.run()
