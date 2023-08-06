class Solution {
    public int serchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        int mid = (start + end) / 2;

        while (start < end) {
            mid = (start + end) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                end = mid;
        }
        return mid;
    }
}

// https://leetcode.com/problems/search-insert-position/solutions/3208460/fastest-java-solution/
public class v2 {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 4, 7 };
        Solution solution = new Solution();
        int ans = solution.serchInsert(nums, 9);
        System.out.println(ans);
    }
}
