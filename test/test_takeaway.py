from lib.takeaway import *
from unittest.mock import Mock, patch
from python import mark

MOCK_STOCK = [
        {"item": "bread", "price": 10},
        {"item": "spinach", "price": 10},
        {"item": "baguette", "price": 14},
        {"item": "peanut butter", "price": 3},
        {"item": "mcDonalds", "price": 18},
]


# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
class TestGetUserOrder:
    @patch("builtins.input", side_effect= [2, 2])


    @mark.it("R")
    def test_get_user_order(mock_input, mock_input_2):
        mock_input.return_value = 2

