class Solution {
    public int pivotIndex(int[] nums) {
        int totalsum = 0, leftsum = 0;
        // Compute total sum
        for (int i = 0; i < nums.length; i++) totalsum += nums[i];
        // Check leftsum == rightsum
        for (int i = 0; i < nums.length; i++) {
            if (leftsum == totalsum - leftsum - nums[i]) return i;
            leftsum += nums[i];
        }
        return -1;
    }
}
