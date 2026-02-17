from lib.takeaway2 import *
from pytest import raises, mark , fixture
from unittest.mock import Mock, patch

MOCK_STOCK = [
    {"item": "bread", "price": 10},
    {"item": "spinach", "price": 10},
    {"item": "baguette", "price": 14},
    {"item": "peanut butter", "price": 3},
    {"item": "mcDonalds", "price": 18},
]


# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
class TestBuildOrders:
    def test_build_order_valid(self):
        choice = 1
        amount = 3
        actual_result = build_order(MOCK_STOCK, choice, amount)
        

        expected_result = {"item": "spinach", "price": 10, "amount": amount}


        assert actual_result == expected_result


    @mark.it("Raises IndexError when an invalid user choice is provided")
    def test_build_order_erros(self):
        ERR_MSG ="User's choice is not within range of stock" 
        amount = 5

        choices = [-1, 100, 50]
        for choice in choices:
            with raises(IndexError, match=ERR_MSG):
                build_order(MOCK_STOCK, choice, amount)

def generate_orders():
    return [
        build_order(MOCK_STOCK, 1, 1),
        build_order(MOCK_STOCK, 2, 2),
    ]


class TestSummariseOrders:
    @mark.it("The summarised orders properly have their total price calculated")
    def test_summarise_orders(self):
        test_generated_orders = generate_orders()
        actual_result, _ = summarise_orders(test_generated_orders)

        for index, order in enumerate(actual_result):
            actual_total_price = order["total_price"]
            test_order = test_generated_orders[index]
            expected_total_price = test_order["price"] * test_order["amount"]

            assert actual_total_price == float(expected_total_price)

    
    @mark.it("The summarise orders properly calculates the total cost of all orders")
    def test_summarise_orders_total_cost(self):
        test_generated_orders = generate_orders()
        _, actual_total_cost = summarise_orders(test_generated_orders)

        expected_total_cost = 0
        for _, order in enumerate(test_generated_orders):
            total_price = order["price"]
            amount = order["amount"]
            expected_total_cost += total_price * amount


        assert actual_total_cost == expected_total_cost




class TestMain():
    def test_main_function(self):
        pass
