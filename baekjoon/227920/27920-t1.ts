// fs 패키지 불러오기
const fs = require("fs");

// input 값 받기
const input_single: number = Number(fs.readFileSync("/dev/stdin").toString());

// 초기 배열
const arr: number[] = [];

// 결과 배열
let result: number[] = [];

// 초기 배열 초기화
for (let i = 1; i <= input_single; i++) {
  // 짝수일 경우 오른쪽 끝으로 보내기
  // 홀수일 경우 왼쪽 끝으로 보내기
  if (i % 2 === 0) arr.push(i);
  else arr.splice(0, 0, i);
}

// 뒤집을 카드의 인덱스
// 초기값 = 1이 적힌 카드의 인덱스
let curr_index: number = arr.indexOf(1);

// 결과 배열 초기화
for (let i = 1; i <= input_single; i++) {
  // 뒤집은 카드의 위치를 결과 배열에 집어넣는다.
  result.push(curr_index + 1);

  // 왼쪽으로 갈지 오르쪽으로 갈지 정한다
  // 후에 뒤집어야 할 카드가 짝수 일 경우 curr_index에 현재 카드의 수 만큼 빼기 아닐경우 더하기
  curr_index += i % 2 === 0 ? -arr[curr_index] : arr[curr_index];
}

// 결과 출력
console.log("YES");
console.log(arr.join(" "));
console.log(result.join(" "));
