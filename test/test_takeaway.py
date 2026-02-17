from lib.takeaway import *
from unittest.mock import Mock, patch

MOCK_STOCK = [
        {"item": "bread", "price": 10},
        {"item": "spinach", "price": 10},
        {"item": "baguette", "price": 14},
        {"item": "peanut butter", "price": 3},
        {"item": "mcDonalds", "price": 18},
]


class TestGetUserOrder:
    @patch("buitlins.input")
    @patch("buitlins.input")
    def test_get_user_order(mock_input, mock_input_2):
        mock_input.return_value = 2
        mock_input_2.return_value = 2

