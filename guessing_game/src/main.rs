use std::io; // import from lib standard, input output.
use std::cmp::Ordering; 
use rand::Rng; // import from lib rand, random number generator.

fn main() { // always have to define a function, main alyways runs first.
    println!("Guess the number."); // print line.

    let secret_number: u32 = rand::thread_rng().gen_range(1..=100); // "let" to make new var, by default is unmutabale ned to add "mut". 
                                                               // from rand lib we chose the thread_rng function (simple rng), and use the gen_range method to get a number in range 1 - 100.
    loop {
   
        println!("Please input your guess.");

        let mut guess = String::new(); // Save guess as empty string (str is reqired for input).

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num, // Use match case on the parse if return ok then set number.
            Err(_) => continue,  // If error continue to next iteretion. "_" is a chachall value for checking for all errors.
        };                                                                          // We use shadowing to turn make a var guess wich is a str to an u32(unasingned 32 bit number)
                                                                                    // we use trim() and parse(). trim method can only be used on strings and removed wide space from beinging and end.
                                                                                    // parse changes the var type to what we specified at the beging (u32), 
                                                                                    
        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {               // match case uses the cmp method that we imported and compaing secret_number.
            Ordering::Less => println!("Too small!"),   // we check if the Ordering less, grather and equal are true and print the output.
            Ordering::Greater => println!("Too big!"),   
            Ordering::Equal => {
                println!("You win!");
                break;                                  // if we win break the loop and end the program.
            }
        }
    }
}

