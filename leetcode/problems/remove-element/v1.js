/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let index = 0;
  for (let j = 0; j < nums.length; j++) {
    if (nums[j] !== val) {
      nums[index++] = nums[j];
    }
  }
  return index;
};

let ans = removeElement([0, 2, 1, 3, 2, 4], 2);
console.log(ans);
