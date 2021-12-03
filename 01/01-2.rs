use std::io;

fn main() {
    let mut window: Vec<u32> = Vec::new();
    let mut last: Option<u32> = None;
    let mut cnt: u32 = 0;
    loop {
        let mut buf = String::new();
        let count = io::stdin().read_line(&mut buf).expect("input error");
        if count == 0 {
            break;
        }
        let val: u32 = buf.trim().parse().expect("input error");
        window.push(val);
        if window.len() == 3 {
            let val = window.iter().sum();
            match last {
                None => {}
                Some(x) => {
                    if x < val {
                        cnt += 1;
                    }
                }
            }
            last = Some(val);
            window.remove(0);
        }
    }
    println!("{}", cnt);
}
