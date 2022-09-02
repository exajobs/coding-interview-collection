import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int minMoves(int[] nums) {
        if (nums.length == 0) return 0;
        Arrays.sort(nums);
        int min_num = nums[0];
        int ans = 0;
        for (int num : nums) {
            ans += num - min_num;
        }
        return ans;
    }
}