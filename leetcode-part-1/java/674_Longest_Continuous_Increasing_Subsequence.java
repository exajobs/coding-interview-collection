class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) return 0;
        int curr = 1, ans = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                curr ++;
                if (curr >= ans) ans = curr;
            } else {
                curr = 1;
            }
        }
        return ans;
    }
}
