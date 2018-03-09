fn is_abundant(x:u32) -> bool {
    let mut sum = 0;

    for n in 1..x {
        if x % n == 0 {
            sum += n;
            // println!("{}", n);
        }
    }

    if sum > x {
        // println!("sum = {}", sum);
        true
    } else {
        false
    }
}

fn main() {
    let mut i = 0;
    for n in 1..28123 {
        if is_abundant(n) {
            i += 1;
            // println!(" {} is abundant!", n);
        }
    }
    println!("Total Abundant numbers are {}", i);
}
