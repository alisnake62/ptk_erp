from legacy import Legacy
from util.date import DateTimeUtil

class ERPUtil:

    current_API = Legacy()
    date_util = DateTimeUtil()

    def _build_stock(self, value:int, product_id: str, product_name: str) -> dict:
        return {
            "value": value,
            "product_id": product_id,
            "product_name": product_name
        }

    def get_stocks(self, sorted_by_volume: bool = True) -> list:
        products = self.current_API.get_products()

        stocks = []
        for product in products:
            stock = self._build_stock(value=product["stock"], product_id=product["id"], product_name=product["name"])
            stocks.append(stock)

        if sorted_by_volume:
            stocks = sorted(stocks, key=lambda d: d['value']) 

        return stocks

    def get_stock(self, product_id: str) -> dict:
        products = self.current_API.get_products()

        for product in products:
            if int(product["id"]) == int(product_id):
                return self._build_stock(value=product["stock"], product_id=product["id"], product_name=product["name"])

    def get_products(self, sorted_by: str=None, color:str=None) -> list:

        if sorted_by not in ["created", "price", None]: raise Exception()

        products = self.current_API.get_products()

        if color is not None:
            products = [product for product in products if product["details"]["color"] == color]

        if sorted_by == "created":
            products = sorted(products, key=lambda d: self.date_util.datetimify(d['createdAt']), reverse=True)

        if sorted_by == "price":
            products = sorted(products, key=lambda d: float(d['details']['price']))

        return products

    def get_product(self, product_id: str) -> dict:
        return self.current_API.get_product(product_id=product_id)