#![allow(unused)]
use std::io;

#[derive(Debug, Clone)]
struct Item {
    name: String,
    quantity: usize,
    price: f32,
    stop: isize,
}

impl Item {
    fn reduce_qty(&mut self, by: usize) {
        self.quantity = self.quantity - by;
    }
}
/// Print a list of dishes
fn main() {
    println!("================ DISHES ===================");

    let chinese_rice = create_item(String::from("Chinese Rice"), 32, 11.45, -10);
    let yoghurt_prime = create_item(String::from("Yoghurt Prime"), 80, 8.97, -10);
    let green_bean = create_item(String::from("Green Bean"), 5, 10.00, -10);

    let mut stock = vec![chinese_rice, yoghurt_prime, green_bean];

    let mut counter = 1;
    for item in stock.iter() {
        println!(
            "|  {counter}  {}       ${}",
            item.name.to_string(),
            item.price,
        );

        counter += 1
    }

    println!("Enter your choice below");
    let selected_item: &mut Item;
    let mut user_choice = String::new();
    loop {
        io::stdin()
            .read_line(&mut user_choice)
            .expect("Error reading from stdin");

        let mut choice: usize = user_choice
            .trim()
            .parse()
            .expect("Could not parse number. Please provide a valid number");

        // index correction
        if choice <= 0 {
            println!("Selected a number out of range, user selected -1 or 0 {choice}");
            return;
        }

        choice = choice - 1;
        if choice >= stock.len() {
            println!("Selected a number out of range, too big {choice}");
            return;
        }
        selected_item = &mut stock[choice];
        break;
    }

    println!("You selected item -> {}", selected_item.name);

    // makes sense to clear the string, because a number was parsed into it
    user_choice.clear();

    println!("Please provide qty");
    loop {
        io::stdin()
            .read_line(&mut user_choice)
            .expect("Error reading from stdin");

        let qty: usize = user_choice.trim().parse().expect("Expected a number");

        if qty >= selected_item.quantity {
            println!(
                "Qty selected too large, must not be more than {}",
                selected_item.quantity
            );
            continue;
        }
        selected_item.reduce_qty(qty);
        break;
    }

    println!("Order has been made");

    println!("Updated stocks: {stock:?}");
}
fn create_item(name: String, qty: usize, price: f32, stop: isize) -> Item {
    return Item {
        name: name,
        quantity: qty,
        price: price,
        stop: stop,
    };
}
