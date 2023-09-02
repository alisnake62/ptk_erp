
from flask import Flask, jsonify
from markupsafe import escape

from util import ERP_Util

erp = ERP_Util()


app = Flask(__name__)

@app.route("/v1/stocks")
def get_stocks():
    return jsonify(erp.get_stocks())

@app.route("/v1/stocks/<product_id>")
def hello(product_id):
    product_id = escape(product_id)

    stock = erp.get_stock(product_id=product_id)

    if stock is None:
        return "stock not found", 404

    return jsonify(stock)

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port=5000)