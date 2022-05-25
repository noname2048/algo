const isPrime = (number) => {
  if (number === 1) return false;
  if (number === 2) return true;
  const max = Math.sqrt(number);
  for (let i = 2; i <= max; i++) {
    if (number % i === 0) return false;
  }
  return true;
};

const solution = (n, k) => {
  let res = 0;

  const arr = n.toString(k).split(/0+/);

  for (let i = 0; i < arr.length; i++) {
    if (isPrime(Number(arr[i]))) res++;
  }
  return res;
};

// 질문게시판에 올라온 질문 나랑 12번 컴파일 에러가 나는게 똑같다.
// 반례 36을 사용하라고 권장해드렸다.
