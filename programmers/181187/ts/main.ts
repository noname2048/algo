const main = () => {
    let answer: number = solution(2, 3);
    console.log(answer);
}

const solution = (r1: number, r2: number): number => {
    let answer = 0;
    for (let x = 1; x <= r2; x++) {
        let y2: number = Math.floor(Math.sqrt(r2**2 - x**2));
        let y1: number = Math.ceil(Math.sqrt(Math.max(0, r1**2 - x**2)));
        answer += y2 - y1 + 1;
    }
    return answer * 4;
}

main();
