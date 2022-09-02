class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ans = 0;
        int curr = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                // Add 1 when encounter 1
                curr++;
                if (curr > ans) ans = curr;
            } else {
                // Set to 0 when encounter 0
                curr = 0;
            }
        }
        return ans;
    }
}
