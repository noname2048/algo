use std::cmp;
use std::f64;

fn main() {
    println!("Hello, world!");
    let answer = solution(2, 3);
    println!("{}", answer);
}

fn solution(r1: i32, r2: i32) -> i32 {
    let mut answer: i32 = 0;
    for x in 1..=r2 {
        let y2: i32 = (f64::from(r2.pow(2) - x.pow(2))).sqrt().floor() as i32;
        let y1: i32 = (f64::from(cmp::max(0, r1.pow(2) - x.pow(2)))).sqrt().ceil() as i32;
        answer += y2 - y1 + 1;
    }
    return answer * 4;
}