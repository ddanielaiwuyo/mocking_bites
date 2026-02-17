"""
    REQUIREMENTS
- See list of dishes and prices
    bread £2, vinegar £10, egg(12) £40

- Select an amout of available disheds:
    bread x4, vinegar x2

- Get an itemised reciept with grandtotal
"""



stock = [
        {"item": "bread", "price": 10},
        {"item": "spinach", "price": 10},
        {"item": "baguette", "price": 14},
        {"item": "peanut butter", "price": 3},
        {"item": "mcDonalds", "price": 18},
]

"""
Shows the main menu displaying all the `stocks`
provided in a formatted way. It returns all the 
orders the user selected and total amount of purchases
on an item
Returns:
    order, {item, price, amount_purchased}
"""
def get_user_order():
    print()
    print("============================================")
    print("   DISPLAYING MENU")
    print("============================================\n")
    selected_item = 0
    while True:
        for i, entry in enumerate(stock, start=1):
            print(f" {i}. {entry['item'].title()}  £{entry['price']}")
        


        print()
        try:
            user_choice = int(input(" Dish Number: "))
            user_choice = user_choice - 1

            if user_choice < 0 or user_choice > len(stock) - 1:
                print(" Please provide a number between 1 and ", len(stock))
                print()
                continue
            else:
                selected_item = user_choice
                break

        except ValueError:
            print(" Please provide a valid number\n")


    print()
    total_amount = 1
    while True:
        try:
            user_amount = int(input(" How many would you like to purchase: "))
            if user_amount <= 0 :
                print(" Please provide an number greater than 0\n")
                continue

            total_amount = user_amount
            break

        except ValueError :
            print(" Please provide a valid number\n")




    item = stock[selected_item]["item"]
    item_price = stock[selected_item]["price"]

    order = {
            "item": item, 
            "price": item_price, 
            "amount_to_purchase": total_amount
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
    list of orders
    total_cost of all orders
"""
def summarise_orders(all_orders):
    summary_orders = []
    item_names: list[str] = []

    total_cost = 0

    for order in all_orders:
        item_name = order["item"]
        item_price = order["price"]
        item_amount = order["amount_to_purchase"]
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
    print("\nCreating Recpeit...\n")

    print(f"   {'ID':>1} {'ITEM':<15} {'PRICE (£)':<5} {'AMOUNT':>3} {'TOTAL (£)':>12}")
    for i, order in enumerate(summarised_orders, start=1):
        template = f"""   {i:<1}. {order['item'].title():<15} £{order['price']:<5}  {order['amount']:>3} {order['total_price']:>12} """

        print(template)


def main():
    try:
        all_orders = []

        order = get_user_order()

        all_orders.append(order)

        while True:
            add_order =  input(" Make another order?[y/n]: ")
            if add_order.lower() in ["y", "yes"]:
                new_order = get_user_order()
                all_orders.append(new_order)
            else:
                break
        
        # tuple unpacking : summarise_orders() returns a tuple()
        summarised_orders, total_cost = summarise_orders(all_orders)
        print_receipt(summarised_orders)


        print(f" \nTotal Cost: £{float(total_cost)}", )
        print()
    except KeyboardInterrupt:
        # for some reason, hitting control-c triggers this
        pass




if __name__ == "__main__":
    main()

