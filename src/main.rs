// https://journey.makers.tech/pages/project-stories
#![allow(unused)]
use std::io;

#[derive(Debug)]
struct Item {
    name: String,
    quantity: usize,
    price: f32,
}

#[derive(Debug)]
struct Receipt {
    username: String,
    total_price: usize,
    item: Item,
    date: String,
}

impl Item {
    fn reduce_qty(&mut self, by: usize) {
        self.quantity = self.quantity - by;
    }
}

fn main() {
    let green_bean = create_item(String::from("Green Bean"), 32, 10.34);
    let hamburger = create_item(String::from("Hamburger"), 20, 8.78);
    let eggs = create_item(String::from("Quail Eggs"), 45, 1.59);

    let mut stock = vec![green_bean, hamburger, eggs];
    let mut i = 1;
    for item in stock.iter() {
        println!(" {i} | {} ${}", item.name, item.price);
        i += 1;
    }
    println!("please provide your choice:");

    let mut user_input = String::new();
    let mut choice: usize = 0;
    loop {
        user_input.clear();
        io::stdin()
            .read_line(&mut user_input)
            .expect("Unxpected error occured trying to read from stdin");

        choice = match user_input.trim().parse::<isize>() {
            Ok(n) => {
                if n <= 0 {
                    println!("number too small");
                    continue;
                }

                choice = n as usize - 1;
                if choice >= stock.len() {
                    println!("choice too big");
                    continue;
                }

                user_input.clear();
                break;
            }
            Err(e) => {
                println!("Couldn't parse -> {}\n Reason: {} ", user_input, e);
                return;
            }
        };
    }

    println!("user_choice {}", choice);
    let selected_item = &mut stock[choice];
    println!("Please provide the amount you would liketo purchase");
    let mut quantity: usize = 1;
    loop {
        user_input.clear();
        io::stdin()
            .read_line(&mut user_input)
            .expect("Unexpected error while trying to read from stdin");

        let qty = match user_input.trim().parse::<isize>() {
            Ok(qty) => {
                if qty <= 0 {
                    println!("Cannot purchase {qty} items, must be positive number!");
                    continue;
                }

                let qty = qty as usize;
                if qty >= selected_item.quantity {
                    println!(
                        "Too much selected, must not be up to {}",
                        selected_item.quantity
                    );
                    continue;
                }

                quantity = qty;
                break;
            }
            Err(e) => {
                println!("Could parse qty amount, please try again: Reasonse {}\n", e);
                continue;
            }
        };
    }

    selected_item.reduce_qty(quantity);
    println!("Upadted : {selected_item:?}");
}

fn create_item(name: String, qty: usize, price: f32) -> Item {
    Item {
        name,
        quantity: qty,
        price,
    }
}
