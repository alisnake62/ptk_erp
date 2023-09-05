from typing import Any
import os

from flask import Flask, jsonify, Request, request

from util.erp import ERPUtil
from util.reseller import ResellerUtil

erp_util = ERPUtil()
reseller_util = ResellerUtil()

app = Flask(__name__)

dev_env = os.getenv("FLASK_DEBUG", "0")
dev_env = True if dev_env == "1" else False

def wrap_result(request: Request, result: Any, reseller: dict) -> str:

    response = {
        "url": request.base_url,
        "reseller": reseller["name"],
        "result": result
    }
    return jsonify(response)

@app.route("/v1/stocks")
def get_stocks():

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    return wrap_result(request=request, result=erp_util.get_stocks(), reseller=reseller)

@app.route("/v1/stocks/<product_id>")
def get_stock(product_id):

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    stock = erp_util.get_stock(product_id=product_id)

    if stock is None:
        return "stock not found", 404

    return wrap_result(request=request, result=stock, reseller=reseller)

@app.route("/v1/products/")
def get_products():

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    args = request.args
    sorted_by = args.get("sorted_by")
    color = args.get("filter_by_color")

    if color is not None:
        color = color.replace('"', '')

    if sorted_by not in ["created", "price", None]:
        return "bad sorted_by argument", 400

    result = erp_util.get_products(sorted_by=sorted_by, color=color)
    return wrap_result(request=request, result=result, reseller=reseller)

@app.route("/v1/products/<product_id>")
def get_product(product_id):

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    product = erp_util.get_product(product_id=product_id)

    if product is None:
        return "product not found", 404

    return wrap_result(request=request, result=product, reseller=reseller)

@app.route("/v1/stock_volume")
def get_stock_volume():

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    return wrap_result(request=request, result=erp_util.get_stock_volume(), reseller=reseller)

@app.route("/v1/stock_volume/<product_id>")
def get_stock_volume_by_product(product_id):

    try:
        token = request.authorization.token
        reseller = reseller_util.get_reseller_by_token(token=token)
    except:
        return "incorrect API token", 403

    stock_volume = erp_util.get_stock_volume_by_product(product_id=product_id)
    return wrap_result(request=request, result=stock_volume, reseller=reseller)


if __name__ == "__main__":
    app.run(debug=dev_env, host = "0.0.0.0", ssl_context='adhoc')