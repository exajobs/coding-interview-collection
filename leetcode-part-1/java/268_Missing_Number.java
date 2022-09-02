class Solution {
    /* public int missingNumber(int[] nums) {
        int n = nums.length;
        int total = n * (n + 1) / 2;
        for (int i = 0; i < nums.length; i++) {
            total -= nums[i];
        }
        return total;
    } */

    public int missingNumber(int[] nums) {
        int res = nums.length;
        for (int i = 0; i < nums.length; i++) {
            res ^= i;
            res ^= nums[i];
        }
        return res;
    }

    /* public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] > mid) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    } */
}
