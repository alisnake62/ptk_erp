from typing import Any
import requests
import json

class Legacy:

    host = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1"
    cache_file_path = "cache_legacy.json"

    def _get_cache(self) -> dict:
        try:
            with open(file=self.cache_file_path, mode="r") as cache_file:
                cache = json.loads(cache_file.read())
            return cache
        except:
            return {}

    def _put_in_cache(self, url: str, data: Any) -> None:
        try:
            with open(file=self.cache_file_path, mode="r") as cache_file:
                cache = json.loads(cache_file.read())
        except:
            cache = {}
        cache[url] = data
        with open(file=self.cache_file_path, mode="w") as cache_file:
            cache_file.write(json.dumps(cache))

    def _get(self, url: str) -> Any:

        cache = self._get_cache()
        if url in cache:
            return cache[url]

        response = requests.get(url=url)
        if response.status_code != 200:
            raise Exception()

        data = response.json()
        self._put_in_cache(url=url, data=data)

        return data

    def get_customers(self) -> list:

        url = f"{self.host}/customers"
        return self._get(url=url)

    def get_customer(self, customer_id: str) -> dict:

        url = f"{self.host}/customers/{customer_id}"
        return self._get(url=url)

    def get_orders(self, customer_id: str) -> list:

        url = f"{self.host}/customers/{customer_id}/orders"
        return self._get(url=url)

    def get_products(self) -> list:

        url = f"{self.host}/products"
        return self._get(url=url)

    def get_product(self, product_id: str) -> dict:

        url = f"{self.host}/products/{product_id}"
        return self._get(url=url)