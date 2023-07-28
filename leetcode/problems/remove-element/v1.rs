pub struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut index = 0;
        for j in 0..nums.len() {
            if nums[j] != val {
                nums[index] = nums[j];
                index += 1
            }
        }
        return index as i32;
    }
}

fn main() {
    let mut nums = vec![0, 1, 2, 3, 2, 4, 2, 5];
    let ans = Solution::remove_element(&mut nums, 2);
    println!("{}", ans);
}
