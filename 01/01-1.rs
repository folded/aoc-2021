use std::io;

fn main() {
    let mut last: Option<u32> = None;
    let mut cnt: u32 = 0;
    loop {
        let mut buf = String::new();
        let count = io::stdin().read_line(&mut buf).expect("input error");
        if count == 0 { break; }
        let val: u32 = buf.trim().parse().expect("input error");
        match last {
            None => {}
            Some(x) => {
                if x < val {
                    cnt += 1;
                }
            }
        }
        last = Some(val);
    }
    println!("{}", cnt);
}