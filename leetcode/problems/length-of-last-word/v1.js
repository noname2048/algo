/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  const words = s.split(" ").filter((item) => item.length > 0);
  const word_len = words.length;
  const last_word = words[word_len - 1];
  return last_word.length;
};

let ans = lengthOfLastWord("   fly  me   to    the    moon   ");
console.log(ans);
