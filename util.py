from legacy import Legacy_API

class ERP_Util:

    current_API = Legacy_API()

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

        stocks = []
        for product in products:
            if int(product["id"]) == int(product_id):
                return self._build_stock(value=product["stock"], product_id=product["id"], product_name=product["name"])