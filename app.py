from flask import Flask, jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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


class news(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(255))
    news_name = db.Column(db.String(255))
    news_content = db.Column(db.Text)
    author = db.Column(db.String(255))
    publish = db.Column(db.String(255))
    origin = db.Column(db.String(255))
    abstract = db.Column(db.String(255))

    def to_json(self):
        json_news = {
            'id': self.id,
            'photo': self.photo,
            'news_name': self.news_name,
            'news_content': self.news_content,
            'author': self.author,
            'publish': self.publish,
            'origin':self.origin,
            "abstract":self.abstract
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


@app.route('/productList')
def productList():
    if urllib.unquote(request.values.get("productname"))=="undefined":
        productname = ""
    else:
        productname = urllib.unquote(request.values.get("productname")) or ""
    return enum(product.query.filter(product.product_name.like('%'+str(productname)+'%')))


@app.route('/newsList')
def newsList():
    return enum(news.query.order_by(-news.id).all())


@app.route('/newsDetail')
def newsDetail():
    newsid = request.values.get("newsid")
    return enum(news.query.filter_by(id=newsid))


# if __name__ == '__main__':
#     app.run()
