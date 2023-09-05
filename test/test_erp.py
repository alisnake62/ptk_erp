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

fake_legacy_customer_7 = {
    "createdAt":"2023-08-29T17:41:41.077Z",
    "name":"Eugene Pfannerstill",
    "username":"Kyle_Sawayn66",
    "firstName":"Dahlia",
    "lastName":"Jaskolski",
    "address":{
        "postalCode":"51160",
        "city":"Phoenix"
    },
    "profile":{
        "firstName":"Vidal",
        "lastName":"Kuhic"
    },
    "company":{
        "companyName":"Harber - Steuber"
    },
    "id":"7",
    "orders":[
        {
            "createdAt":"2023-08-30T10:54:50.688Z",
            "id":"1",
            "customerId":"7"
        },
        {
            "createdAt":"2023-08-29T17:17:39.378Z",
            "id":"51",
            "customerId":"7"
        }
    ]
}
fake_legacy_customer_12 = {
    "createdAt":"2023-08-30T17:41:41.077Z",
    "name":"Martin Dupont",
    "username":"martinmatin",
    "firstName":"Martin",
    "lastName":"Dupont",
    "address":{
        "postalCode":"31400",
        "city":"Toulouse"
    },
    "profile":{
        "firstName":"Martin",
        "lastName":"Dupont"
    },
    "company":{
        "companyName":"Rubik's Cube Corporacy"
    },
    "id":"12",
    "orders":[
        {
            "createdAt":"2023-08-27T10:54:50.688Z",
            "id":"3",
            "customerId":"12"
        }
    ]
}

fake_legacy_order_1 = {
    "createdAt":"2023-08-30T10:54:50.688Z",
    "id":"1",
    "customerId":"7",
    "products":[
        fake_legacy_product_3,
        fake_legacy_product_53
    ]
}
fake_legacy_order_51 = {
    "createdAt":"2023-08-29T17:17:39.378Z",
    "id":"51",
    "customerId":"7",
    "products":[]
}
fake_legacy_order_3 = {
    "createdAt":"2023-08-27T10:54:50.688Z",
    "id":"3",
    "customerId":"12",
    "products":[
        fake_legacy_product_26
    ]
}

fake_legacy_products = [
    fake_legacy_product_3,
    fake_legacy_product_53,
    fake_legacy_product_26
]

fake_legacy_customers = [
    fake_legacy_customer_7,
    fake_legacy_customer_12
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

    def test_get_stock_volume(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_products.return_value = fake_legacy_products

        stock_volume = erp_util.get_stock_volume()

        assert stock_volume == 73254 + 1609 + 2464

    def test_get_stock_volume_by_product(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_product.return_value = fake_legacy_product_3

        stock_volume = erp_util.get_stock_volume_by_product(product_id="3")

        assert stock_volume == 73254

    def test_get_orders(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_customers.return_value = fake_legacy_customers
        erp_util.current_API.get_orders.side_effect = [[fake_legacy_order_1, fake_legacy_order_51], [fake_legacy_order_3]]

        orders = erp_util.get_orders()

        expected_orders = [
            fake_legacy_order_1,
            fake_legacy_order_51,
            fake_legacy_order_3
        ]

        assert orders == expected_orders

    def test_get_order(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_customers.return_value = fake_legacy_customers
        erp_util.current_API.get_orders.side_effect = [[fake_legacy_order_1, fake_legacy_order_51], [fake_legacy_order_3]]

        orders = erp_util.get_order(order_id = "1")

        assert orders == fake_legacy_order_1

    def test_get_order_products(self, mocker):

        erp_util = ERPUtil()
        erp_util.current_API = mocker.MagicMock()
        erp_util.current_API.get_customers.return_value = fake_legacy_customers
        erp_util.current_API.get_orders.side_effect = [[fake_legacy_order_1, fake_legacy_order_51], [fake_legacy_order_3]]

        products = erp_util.get_order_products(order_id="1")

        expected_products = [
            fake_legacy_product_3,
            fake_legacy_product_53
        ]

        assert products == expected_products