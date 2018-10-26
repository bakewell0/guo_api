from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "url": "http://img07.yiguoimg.com/d/others/180213/9288719443928141.jpg",
        "id": 1,
        "upc": "666",
        "title": "666"
    }
]


@app.route('/products', methods=['GET'])
def get_tasks():
    return jsonify({'products': products})



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
