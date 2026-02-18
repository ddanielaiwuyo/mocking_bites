from lib.main import App
from lib.order import OrderEntry
from pytest import raises, mark, fixture 
from unittest.mock import Mock, patch
"""
Application Flow:
    Prompts user to select an item from the stock
    get_user_choice(stock: list) -> int

    Prompts user to put how much of an item they want
    get_quantity() -> int

    Appends to the list of order_entries
    add_order_entries(stock, user_choice, quantity) -> None

    Calculates the total price for each OrderEntry by OrderEntry.calculate_total_price()
    summarise_orders() -> None
"""

class TestApplicationInitiation:
    @mark.it("Properly initialises expected properties of class")
    def test_app_init(self):
        stock = [OrderEntry("tuna", 50)]
        app = App(stock)

        assert app.stock == stock
        assert app.order_entries == []

    @mark.it("Raises TypeError if  stock is not a list type")
    def test_app_init_raises_error(self):
        invalid_stock = Mock()

        expected_err = "The 'stock' must be a list of Orders"
        with raises(TypeError, match=expected_err):
            App(invalid_stock)

    @mark.it("Raises TypeError if the list of stock does not contain 'OrderEntry' classes")
    def test_app_init_raises_error(self):
        invalid_stock = [{"invalid_order_entry": "tuna", "price": 32}]

        expected_err = "All orders must be of type OrderEntry, got:"
        with raises(TypeError, match=expected_err):
            App(invalid_stock)



class TestGetUserChoice:
    @mark.it("Returns a zero based index based on amount of stock provided, and user_choice")
    @patch("builtins.input", return_value=1)
    @patch("lib.main.isinstance", return_value=True)
    def test_get_user_choice_valid(self, mock_input, mock_type_check):
        mock_order = Mock()
        mock_order.name = "Mock Tuna"
        mock_order.price = 14
        mock_order.quantiy = 1
        
        app = App([mock_order])
        actual_result = app.get_user_choice()
        assert actual_result ==  0
        

class TestAddNewOrder:
    @patch("lib.main.App._get_quantity", return_value = 3)
    def test_new_order(self, mock_get_quantity):
        # mock_order = o
        # mock_order.name = "Vitamin C"
        # mock_order.price = 13
        # mock_order.quantiy = 1
        # mock_order_2 = Mock()
        # mock_order_2.name = "Honey"
        # mock_order_2.price = 2
        # mock_order_2.quantity = 1
        # mock_stock = [mock_order, mock_order_2]
        # app.order_entries.append(mock_order)

        stock = [OrderEntry("Tea and Milk", 8), OrderEntry("Honey", 12)]
        app = App(stock)

        app.add_new_order(1)

        expected_result = [stock[1]]
        assert app.order_entries == expected_result




    @mark.it("Get Quantity is called when the adding a new order")
    @patch("lib.main.App._get_quantity", return_value = 3)
    def test_new_order(self, mock_get_quantity):
        order_entry_1 = OrderEntry("Tea and Milk", 8)
        order_entry_2 = OrderEntry("Honey", 12)

        stock = [order_entry_1, order_entry_2]
        app = App(stock)
        app.add_new_order(1)

        # app.get_quantity = Mock(return_value = 3)
        # app._get_quantity.assert_called_once()
        mock_get_quantity.assert_called_once()

        # also check if the order entry had it's quantity updated
        assert app.order_entries[0].quantity == 3





class TestSummarisedOrders:
    @mark.it("All orders have their total price calculated")
    def test_summarised_orders(self):
        order_entry_1 = OrderEntry("Tea and Milk", 8)
        order_entry_2 = OrderEntry("Honey", 12)

        # assuming that the user only bought 1 for each item
        order_entry_1.calculate_total_price = Mock(return_value = 8)
        order_entry_2.calculate_total_price = Mock(return_value = 12)

        stock = [order_entry_1, order_entry_2]
        app = App(stock)
        app._get_quantity = Mock(return_value = 1)
        app.add_new_order(0)
        app.add_new_order(1)

        app.get_summarised_orders()

        order_entry_1.calculate_total_price.assert_called_once()
        order_entry_2.calculate_total_price.assert_called_once()


        assert order_entry_1.total_price == 8
        assert order_entry_2.total_price == 12

        
    @mark.it("All orders should have their total price calculated with multiple quantities")
    @patch("lib.main.App._get_quantity", side_effect = [ 3, 4 ])
    def test_summarised_orders_multiple_quantity(self, mock_get_qty):
        order_entry_1 = OrderEntry("Tea and Milk", 8)
        order_entry_2 = OrderEntry("Honey", 12)

        stock = [order_entry_1, order_entry_2]
        app = App(stock)
        app.add_new_order(0)
        app.add_new_order(1)

        app.get_summarised_orders()
        assert order_entry_1.total_price == 8 * 3
        assert order_entry_2.total_price == 12 * 4


