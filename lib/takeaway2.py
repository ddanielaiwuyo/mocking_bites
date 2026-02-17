"""
    REQUIREMENTS
- See list of dishes and prices, for example
    bread £2, vinegar £10, egg(12) £40

- Select an amout of available disheds:
    bread x4, vinegar x2

- Get an itemised reciept with grandtotal
"""

"""
Shows the main menu displaying all the `stocks`
provided in a formatted way.
Returns:
    None
"""
def print_menu(stock):
    print("\n============================================")
    print("   DISPLAYING MENU")
    print("============================================\n")
    for i, entry in enumerate(stock, start=1):
        print(f" {i}. {entry['item'].title()}  £{entry['price']}")
        



"""
It returns all the 
orders the user selected and total amount of purchases
on an item
Returns:
    order, {item, price, amount_purchased}
"""
def get_user_order(stock):
    while True:
        try:
            user_choice = int(input(" Dish Number: "))
            user_choice = user_choice - 1

            if user_choice < 0 or user_choice > len(stock) - 1:
                print(" Please provide a number between 1 and ", len(stock))
                print()
                continue
            else:
                selected_item = user_choice
                return selected_item

        except ValueError:
            print(" Please provide a valid number\n")

"""
Returns the numbner of items the user 
wants to purchase, by prompting.
Returns:
    int
"""
def get_order_amount():
    while True:
        try:
            order_amount = int(input(" How many would you like to purchase: "))
            if order_amount <= 0 :
                print(" Please provide an number greater than 0\n")
                continue

            # total_amount = user_amount
            return order_amount

        except ValueError :
            print(" Please provide a valid number\n")



"""
Uses the stock, user_choice, and number of items 
they want to to buy for a particular and returns an
order entry, order.
Returns:
    dictionary: {item, price, order_amount}
"""
def build_order(stock, user_choice, order_amount):
    # if not isinstance(user_choice, int):
    #     raise TypeError(" Unexpected error, users_choice is not an integer: ", type(user_choice))
    # elif not isinstance(order_amount, int):
    #     raise TypeError(" Unexpected error, order_amount is not an integer: ", type(order_amount))
    # elif not isinstance(stock, list):
    #     raise TypeError(" Unexpected error, stock is not a list, type: ", type(stock))
    #
    if user_choice < 0 or user_choice >= len(stock):
        raise IndexError("User's choice is not within range of stock")
    item = stock[user_choice]["item"]
    item_price = stock[user_choice]["price"]

    order = {
            "item": item, 
            "price": item_price, 
            "amount": order_amount
           }
    return order


"""
Takes all orders and transforms them into
a summary datastructure:
    in: [{item, price, amount_to_purchase}]
    out: [{item, price, amount_to_purchase, total_price}]

It also returns the total cost of all purchases made
by the user
Returns:
    tuple(list of orders, total_cost of all orders)
"""
def summarise_orders(all_orders):
    summary_orders = []

    total_cost = 0

    for order in all_orders:
        item_name = order["item"]
        item_price = order["price"]
        item_amount = order["amount"]
        total_price = item_price * item_amount

        
        summary_data = {"item": item_name,
                        "price": float(item_price),
                        "amount": item_amount,
                        "total_price": float(total_price),
                        }

        summary_orders.append(summary_data)
        total_cost += total_price


    
    return (summary_orders, total_cost)

def print_receipt(summarised_orders):
    print("\nCreating Recepit...\n")

    print(f"   {'ID':>1} {'ITEM':<15} {'PRICE (£)':<5} {'AMOUNT':>3} {'TOTAL (£)':>12}")
    for i, order in enumerate(summarised_orders, start=1):
        template = f"""
        {i:<1}. {order['item'].title():<15} £{order['price']:<5}
        {order['amount']:>3} {order['total_price']:>12} """

        print(template)

def main():
    stock = [ 
        {"item": "bread", "price": 10},
        {"item": "spinach", "price": 10},
        {"item": "baguette", "price": 14},
        {"item": "peanut butter", "price": 3},
        {"item": "mcDonalds", "price": 18},
    ]
    ALL_ORDERS = []
    try:
        while True:
            print_menu(stock)
            user_choice = get_user_order(stock)
            order_amount = get_order_amount()
            new_order = build_order(stock, user_choice, order_amount)

            add_order =  input(" Make another order?[y/n]: ")
            ALL_ORDERS.append(new_order)
            if add_order.lower() in ["y", "yes"]:
                continue
            else:
                break

        summarised_orders, total_cost = summarise_orders(ALL_ORDERS)
        print_receipt(summarised_orders)

        print(f"\n Total Cost: £{float(total_cost)}")
    except KeyboardInterrupt:
        print("\n Quitting Takeaway\n")




if __name__ == "__main__":
    main()
