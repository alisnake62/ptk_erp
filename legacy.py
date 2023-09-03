import requests

class Legacy:

    host = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1"

    def _request(self, url: str):
        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception

        return response.json()

    def get_customers(self) -> list:

        url = f"{self.host}/customers"
        return self._request(url=url)

    def get_customer(self, customer_id: str) -> dict:

        url = f"{self.host}/customers/{customer_id}"
        return self._request(url=url)

    def get_orders(self, customer_id: str) -> list:

        url = f"{self.host}/customers/{customer_id}/orders"
        return self._request(url=url)

    def get_products(self) -> list:

        url = f"{self.host}/products"
        return self._request(url=url)

    def get_product(self, product_id: str) -> dict:

        url = f"{self.host}/products/{product_id}"
        return self._request(url=url)