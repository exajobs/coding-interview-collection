class Solution {
    /* public boolean checkPossibility(int[] nums) {
        int pos = -1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                // More than two broken points
                if (pos != -1) return false;
                pos = i;
            }
        }
        if (pos == -1 || pos == 0 || pos == nums.length - 2) return true;
        // Remove pos or pos + 1
        return (nums[pos - 1] <= nums[pos + 1] || nums[pos] <= nums[pos + 2]);
    } */

    public boolean checkPossibility(int[] nums) {
        int brokenPoint = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                brokenPoint++;
                if (brokenPoint >= 2) return false;
                // Remove i or remove i + 1
                if (i - 1 < 0 || nums[i - 1] <= nums[i + 1]) nums[i] = nums[i + 1];
                else nums[i + 1] = nums[i];
            }
        }
        return true;
    }
}
