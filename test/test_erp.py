from util.erp import ERPUtil

fake_legacy_product_3 = {
    "createdAt":"2023-08-28T03:16:28.440Z",
    "name":"Rufus Pacocha",
    "details":{
        "price":"97.00",
        "description":"The Football Is Good For Training And Recreational Purposes",
        "color":"red"
    },
    "stock":73254,
    "id":"3"
}
fake_legacy_product_53 = {
    "createdAt":"2023-08-29T22:55:14.728Z",
    "name":"Paula Hodkiewicz",
    "details":{
        "price":"139.00",
        "description":"The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
        "color":"salmon"
    },
    "stock":1609,
    "id":"53"
}
fake_legacy_product_26 = {
    "createdAt":"2023-08-27T22:55:14.728Z",
    "name":"Titi",
    "details":{
        "price":"39.00",
        "description":"Un incroyable produit",
        "color":"purple"
    },
    "stock":2464,
    "id":"26"
}
# test
fake_legacy_products = [
    fake_legacy_product_3,
    fake_legacy_product_53,
    fake_legacy_product_26
]

class TestERP:

    def test_get_stocks(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        stocks = erp_util.get_stocks()

        expected_stocks = [
            {
                "value": 1609,
                "product_id": "53",
                "product_name": "Paula Hodkiewicz"
            },
            {
                "value": 2464,
                "product_id": "26",
                "product_name": "Titi"
            },
            {
                "value": 73254,
                "product_id": "3",
                "product_name": "Rufus Pacocha"
            }
        ]

        assert stocks == expected_stocks

    def test_get_stock(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        stock = erp_util.get_stock(product_id="53")

        expected_stock = {
            "value": 1609,
            "product_id": "53",
            "product_name": "Paula Hodkiewicz"
        }

        assert stock == expected_stock


    def test_get_products_sorted_by_created(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        products = erp_util.get_products(sorted_by="created")

        expected_products = [
            {
                "createdAt":"2023-08-29T22:55:14.728Z",
                "name":"Paula Hodkiewicz",
                "details":{
                    "price":"139.00",
                    "description":"The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
                    "color":"salmon"
                },
                "stock":1609,
                "id":"53"
            },
            {
                "createdAt":"2023-08-28T03:16:28.440Z",
                "name":"Rufus Pacocha",
                "details":{
                    "price":"97.00",
                    "description":"The Football Is Good For Training And Recreational Purposes",
                    "color":"red"
                },
                "stock":73254,
                "id":"3"
            },
            {
                "createdAt":"2023-08-27T22:55:14.728Z",
                "name":"Titi",
                "details":{
                    "price":"39.00",
                    "description":"Un incroyable produit",
                    "color":"purple"
                },
                "stock":2464,
                "id":"26"
            }
        ]

        assert products == expected_products

    def test_get_products_sorted_by_price(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        products = erp_util.get_products(sorted_by="price")

        expected_products = [
            {
                "createdAt":"2023-08-27T22:55:14.728Z",
                "name":"Titi",
                "details":{
                    "price":"39.00",
                    "description":"Un incroyable produit",
                    "color":"purple"
                },
                "stock":2464,
                "id":"26"
            },
            {
                "createdAt":"2023-08-28T03:16:28.440Z",
                "name":"Rufus Pacocha",
                "details":{
                    "price":"97.00",
                    "description":"The Football Is Good For Training And Recreational Purposes",
                    "color":"red"
                },
                "stock":73254,
                "id":"3"
            },
            {
                "createdAt":"2023-08-29T22:55:14.728Z",
                "name":"Paula Hodkiewicz",
                "details":{
                    "price":"139.00",
                    "description":"The beautiful range of Apple Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
                    "color":"salmon"
                },
                "stock":1609,
                "id":"53"
            }
        ]

        assert products == expected_products

    def test_get_products_filter_by_color(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        products = erp_util.get_products(color="purple")

        expected_products = [
            {
                "createdAt":"2023-08-27T22:55:14.728Z",
                "name":"Titi",
                "details":{
                    "price":"39.00",
                    "description":"Un incroyable produit",
                    "color":"purple"
                },
                "stock":2464,
                "id":"26"
            }
        ]

        assert products == expected_products

    def test_get_product(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_product.return_value = fake_legacy_product_26
        product = erp_util.get_product(product_id="26")

        expected_product = fake_legacy_product_26

        assert product == expected_product

    def test_get_orders(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products
        products = erp_util.get_products(color="purple")

        expected_products = [
            {
                "createdAt":"2023-08-27T22:55:14.728Z",
                "name":"Titi",
                "details":{
                    "price":"39.00",
                    "description":"Un incroyable produit",
                    "color":"purple"
                },
                "stock":2464,
                "id":"26"
            }
        ]

        assert products == expected_products