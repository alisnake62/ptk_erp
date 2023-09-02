
from flask import Flask, jsonify, request

from util.erp import ERPUtil

erp = ERPUtil()


app = Flask(__name__)

@app.route("/v1/stocks")
def get_stocks():
    return jsonify(erp.get_stocks())

@app.route("/v1/stocks/<product_id>")
def get_stock(product_id):

    stock = erp.get_stock(product_id=product_id)

    if stock is None:
        return "stock not found", 404

    return jsonify(stock)

@app.route("/v1/products/")
def get_products():

    args = request.args
    sorted_by = args.get("sorted_by")

    if sorted_by not in ["created", "price", None]:
        return "bad sorted_by argument", 400

    return jsonify(erp.get_products(sorted_by=sorted_by))

@app.route("/v1/products/<product_id>")
def get_product(product_id):

    product = erp.get_product(product_id=product_id)

    if product is None:
        return "product not found", 404

    return jsonify(product)



if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port=5000)