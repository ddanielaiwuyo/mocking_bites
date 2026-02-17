class OrderEntry:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError("Name must be string!")

        if not isinstance(price, int):
            raise TypeError("Price must be an int!")

        self.name = name
        self.price = price
        self.quantity = 1
    
        self.total_price = self.price * self.quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def update_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError(" Quantity must be an int!")

        # ignore such values and leave as default
        # might be handy if we wanted to reduce it
        if quantity <= 0:
            return
        self.quantity = quantity


