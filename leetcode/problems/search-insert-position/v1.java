class Solution {
    public int serchInsert(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        int mid = (start + end)  / 2;
        while (start < end) {
            if (nums[mid] == target) return mid;
            else if(nums[mid] < target) {
                start = mid + 1;
                mid = (start + end) / 2;
            }
            else {
                end = mid;
                mid = (start + end) / 2;
            }
        }
        return mid;
    }
}

public class v1 {
    public static void main(String[] args) {
        int[] nums = {1,2,4,7};
        Solution solution = new Solution();
        int ans = solution.serchInsert(nums, 9);
        System.out.println(ans);
    }
}