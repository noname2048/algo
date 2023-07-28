class Solution {
    public int removeElement(int[] nums, int val) {
        int index = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[index++] = nums[j];
            }
        }
        return index;
    }
}

public class v1 {
    public static void main(String[] args) {
        int[] problem = {0, 2, 1, 2, 3, 2};
        Solution solution = new Solution();
        int ans = solution.removeElement(problem, 2);
        System.out.println(ans);
    }
}

/**
 * javac v1.java
 * java v1
 * >> Hello World!!
 * (or just use code runner and play button)
 */
