/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  const strLen = s.length;
  let counter = 0;
  for (let i = strLen - 1; i >= 0; i--) {
    if (s[i] === " " && counter > 0) {
      return counter;
    } else if (s[i] !== " ") counter++;
  }
  return counter;
};

let ans = lengthOfLastWord("  fly  me   to    the    moon   ");
console.log(ans);
