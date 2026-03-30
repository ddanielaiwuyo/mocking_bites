// https://journey.makers.tech/pages/project-stories
#![allow(unused)]
use std::io;
use std::fs::File;
use std::io::Write;

#[derive(Debug, Clone)]
struct Item {
    name: String,
    quantity: usize,
    price: f32,
}

#[derive(Debug)]
struct Receipt {
    username: String,
    order: Order
}

#[derive(Debug)]
struct Order {
    quantity: usize,
    item_name: String,
    item_price: f32,
}

impl Item {
    fn reduce_qty(&mut self, by: usize) {
        self.quantity = self.quantity - by;
    }
}

impl Order {
    fn calculate_total_price(&self) -> f32 {
        self.item_price  * self.quantity as f32
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

        match user_input.trim().parse::<isize>() {
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
                println!("Could parse qty amount, please try again: Reason {}\n", e);
                continue;
            }
        };
    }

    selected_item.reduce_qty(quantity);
    println!("Please provide username");

    user_input.clear();
    io::stdin().read_line(&mut user_input).expect("Error occured reading from stdin");

    let reciept =  Receipt {
        username: user_input.trim().to_string(),
        order: Order { 
        quantity: quantity,
        item_name: selected_item.name.clone(),
        item_price: selected_item.price,
    },
    };

    println!("Receipt -> : {reciept:?}");
    save_to_file(reciept);
}

fn save_to_file(r: Receipt){
    let mut fh = File::options().append(true).open("receipts.txt").expect("Could not open receipts.txt file");
    writeln!(&mut fh, "{r:?}");
}

fn create_item(name: String, qty: usize, price: f32) -> Item {
    Item {
        name,
        quantity: qty,
        price,
    }
}
