class Solution {
    public int serchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        int mid;

        while (start < end) {
            mid = (start + end) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                end = mid;
        }
        return start;
    }
}

public class v3 {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 4, 7 };
        Solution solution = new Solution();
        int ans = solution.serchInsert(nums, 9);
        System.out.println(ans);
    }
}
