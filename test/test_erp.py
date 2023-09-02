import pytest

from util import ERP_Util

fake_legacy_products = [
    {
        "createdAt":"2023-08-30T03:16:28.440Z",
        "name":"Rufus Pacocha",
        "details":{
            "price":"97.00",
            "description":"The Football Is Good For Training And Recreational Purposes",
            "color":"red"
        },"stock":73254,
        "id":"3",
        "orderId":"3"
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
        "id":"53",
        "orderId":"3"
    }
]

class TestERP:

    def test_True(self, mocker):
        assert False # Test 4

    def test_get_stocks(self, mocker):

        erp = ERP_Util()
        erp.current_API = mocker.MagicMock()
        erp.current_API.get_products.return_value = fake_legacy_products
        stocks = erp.get_stocks()

        expected_stock = [
            {
                "value": 73254,
                "product_id": "3",
                "product_name": "Rufus Pacocha"
            },
            {
                "value": 1609,
                "product_id": "53",
                "product_name": "Paula Hodkiewicz"
            }
        ]

        assert stocks == expected_stock