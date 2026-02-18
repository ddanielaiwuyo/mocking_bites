from .order import OrderEntry

class App():
    def __init__(self, stock):
        if not isinstance(stock, list):
            raise TypeError("The 'stock' must be a list of Orders")

        self.__validate_stock(stock)

        self.stock = stock
        self.order_entries = []

    def print_menu(self):
        print("\n============================================")
        print("   DISPLAYING MENU")
        print("============================================\n")
        for i, order in enumerate(self.stock, start=1):
            print(f" {i}. {order.name}  £{order.price}")


    """
    Prompts user to select an item from the stock.
    Returns the 0 based index based on the stock provided
    `get_user_choice(stock: list) -> int`
    """
    def get_user_choice(self):
        while True:
            try:
                user_choice = int(input(" Dish Number: "))
                user_choice = user_choice - 1

                if user_choice < 0 or user_choice > len(self.stock) - 1:
                    print(" Please provide a number between 1 and ", len(self.stock))
                    print()
                    continue
                else:
                    return user_choice

            except ValueError:
                print(" Please provide a valid number\n")

    """
    Prompts user to put how much of an item they want
    `get_quantity() -> int`
    """
    def _get_quantity(self):
        while True:
            try:
                order_amount = int(input(" How many would you like to purchase: "))
                if order_amount <= 0 :
                    print(" Please provide an number greater than 0\n")
                    continue

                return order_amount

            except ValueError :
                print(" Please provide a valid number\n")

    """
    Appends to the list of order_entries. By calling the
    `_get_quantity()` method, it updates the Order 
    `add_order_entries(stock, user_choice, quantity) -> None`
    """
    def add_new_order(self, user_choice):
        quantity = self._get_quantity()
        new_order = self.stock[user_choice]
        new_order.update_quantity(quantity)
        new_order.total_price = quantity * new_order.price

        self.order_entries.append(self.stock[user_choice])


    def get_summarised_orders(self):
        # so that we still have the initial state
        # of all orders, we'll return a copy here
        # summarised_orders = self.order_entries
        for order in self.order_entries:
            order.total_price = order.calculate_total_price()
        

    def calculate_total_cost(self):
        total = 0
        for order in self.order_entries:
            total += order.total_price

        return total

    def print_reciept(self):
        print("\nCreating Recepit...\n")

        print(f"   {'ID':>1} {'ITEM':<15} {'PRICE(£)':<5} {'AMOUNT':>3} {'TOTAL(£)':>12}")
        for i, order in enumerate(self.order_entries, start=1):
            template = f"""   {i:<1}. {order.name:<15} £{order.price:<5}  {order.quantity:>3} {order.total_price:>12}"""

            print(template)




    def __validate_stock(self, stock):
        for order in stock:
            if not isinstance(order, OrderEntry):
                raise TypeError( "All orders must be of type OrderEntry, got:", order, type(order))



def main():
    stock = [ OrderEntry("Tuna", 2), OrderEntry("Bread", 10),
            OrderEntry("Creatine", 30), OrderEntry("Shrimp", 14) ]

    app = App(stock)
    try:
        while True:
            app.print_menu()
            user_choice = app.get_user_choice()
            app.add_new_order(user_choice)
            
            add_order =  input(" Make another order?[y/n]: ")

            if add_order.lower() in ["y", "yes"]:
                continue
            else:
                break

        app.print_reciept()
        total_cost = app.calculate_total_cost()
        print(f"\nTotal Cost: £{total_cost}")
        print()
    except KeyboardInterrupt:
        print(" Closing Applicasiion\n")
    except Exception as err:
        print(" Unexpected error occured")
        print(err)



if __name__ == "__main__":
    main()
