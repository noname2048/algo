
class Solution {
    public int strStr(String haystack, String needle) {
        int i = 0;
        while (i < haystack.length()) {
            int j = 0;
            while (j < needle.length()) {
                if (haystack.charAt(i + j)!= needle.charAt(j)) break;
                j++;
                if (j == needle.length()) {
                    return i;
                }
                if (i + j == haystack.length()) {
                    return -1;
                }
            }
            i++;
        }
        return -1;
    }
}

public class v1 {
    public static void main(String args[]) {
        Solution solution = new Solution();
        int ans = solution.strStr("subsubsub", "sub");
        System.out.println(ans);
    }
}
