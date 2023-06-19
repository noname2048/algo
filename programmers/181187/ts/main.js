"use strict";
const main = () => {
    let answer = 0;
    answer = solution(2, 3);
    console.log(answer);
};
const solution = (r1, r2) => {
    let answer = 0;
    for (let x = 1; x <= r2; x++) {
        let y2 = Math.floor(Math.sqrt(r2 ** 2 - x ** 2));
        let y1 = Math.ceil(Math.sqrt(r1 ** 2 - x ** 2));
        answer += y2 - y1 + 1;
    }
    return answer * 4;
};
