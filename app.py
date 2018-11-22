from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import urllib
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
CORS(app, supports_credentials=True)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Zjb1234.@47.99.44.43:3306/guo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123aaa@127.0.0.1:3306/guo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))

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

    def __init__(self, photo, product_name, product_desc, old_price, price, volume, warehouse, catalog, origin, sales,
                 spec, weight, pack, period, storage, activity, scan):
        self.photo = photo
        self.product_name = product_name
        self.product_desc = product_desc
        self.old_price = old_price
        self.price = price
        self.volume = volume
        self.warehouse = warehouse
        self.catalog = catalog
        self.origin = origin
        self.sales = sales
        self.spec = spec
        self.weight = weight
        self.pack = pack
        self.period = period
        self.storage = storage
        self.activity = activity
        self.scan = scan

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
            "spec": self.spec,
            "weight": self.spec,
            "pack": self.pack,
            "period": self.period,
            "storage": self.storage,
            "activity": self.activity,
            "scan": self.scan,
            "create_time": self.create_time
        }
        return json_product


class news(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(255))
    news_name = db.Column(db.String(255))
    news_content = db.Column(db.Text)
    author = db.Column(db.String(255))
    publish = db.Column(db.String(255))
    origin = db.Column(db.String(255))
    abstract = db.Column(db.String(255))

    def __init__(self, photo, news_name, news_content, author, origin, abstract):
        self.photo = photo
        self.news_name = news_name
        self.news_content = news_content
        self.author = author
        # self.publish = publish
        self.origin = origin
        self.abstract = abstract

    def to_json(self):
        json_news = {
            'id': self.id,
            'photo': self.photo,
            'news_name': self.news_name,
            'news_content': self.news_content,
            'author': self.author,
            # 'publish': self.publish,
            'origin': self.origin,
            "abstract": self.abstract
        }
        return json_news


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


@app.route('/addProduct', methods=['POST'])
def addProduct():
    photo = request.json["photo"]
    product_name = request.json["product_name"]
    product_desc = request.json["product_desc"]
    old_price = request.json["old_price"]
    price = request.json["price"]
    volume = request.json["volume"]
    warehouse = request.json["warehouse"]
    catalog = request.json["catalog"]
    origin = request.json["origin"]
    sales = request.json["sales"]
    spec = request.json["spec"]
    weight = request.json["weight"]
    pack = request.json["pack"]
    period = request.json["period"]
    storage = request.json["storage"]
    activity = request.json["activity"]
    scan = request.json["scan"]

    db.session.add(
        product(photo, product_name, product_desc, old_price, price, volume, warehouse, catalog, origin, sales, spec,
                weight, pack, period, storage, activity, scan))
    db.session.commit()
    return jsonify({"isSuccess": True})

@app.route('/delProduct', methods=['POST'])
def delProduct():
    productid = request.json["productid"]
    p = product.query.filter_by(id=productid).first()
    db.session.delete(p)
    db.session.commit()
    return jsonify({"isSuccess": True})

@app.route('/productList')
def productList():
    if urllib.unquote(request.values.get("productname")) == "undefined":
        productname = ""
    else:
        productname = urllib.unquote(request.values.get("productname")) or ""
    return enum(product.query.filter(product.product_name.like('%' + str(productname) + '%')))


@app.route('/newsList')
def newsList():
    return enum(news.query.order_by(news.id.desc()).all())


@app.route('/newsDetail')
def newsDetail():
    newsid = request.values.get("newsid")
    return enum(news.query.filter_by(id=newsid))


@app.route('/addNews', methods=['POST'])
def addNews():
    photo = request.json["photo"]
    news_name = request.json["news_name"]
    news_content = request.json["news_content"]
    author = request.json["author"]
    origin = request.json["origin"]
    abstract = request.json["abstract"]

    db.session.add(news(photo, news_name, news_content, author, origin, abstract))
    db.session.commit()
    return jsonify({"isSuccess": True})

@app.route('/delNews', methods=['POST'])
def delNews():
    newsid = request.json["newsid"]
    n = news.query.filter_by(id=newsid).first()
    db.session.delete(n)
    db.session.commit()
    return jsonify({"isSuccess": True})


@app.route('/up_photo', methods=['POST'], strict_slashes=False)
def api_upload():
    img = request.files['photo']
    file_path = os.path.join(basedir,"./upload",img.filename)
    img.save(file_path)
    return jsonify({"isSuccess": True})


if __name__ == '__main__':
    app.run()
