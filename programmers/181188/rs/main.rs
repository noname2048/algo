fn main() {
    let targets = vec![
        vec![4, 5],
        vec![4, 8],
        vec![10, 14],
        vec![11, 13],
        vec![5, 12],
        vec![3, 7],
        vec![1, 4]
    ];

    println!("{}", solution(targets));
}

fn solution(mut targets: Vec<Vec<i32>>) -> i32 {
    let mut answer: i32 = 0;
    targets.sort_by(|a, b| a[1].cmp(&b[1]));

    let mut available_fire_pos: i32 = 0;
    for target in &targets {
        if available_fire_pos <= target[0] {
            answer += 1;
            available_fire_pos = target[1];
        }
    }

    return answer;
}
