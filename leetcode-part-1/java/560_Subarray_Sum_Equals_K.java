public class Solution {
    /*public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum = 0;
            for (int end = start; end < nums.length; end++) {
                sum += nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }*/
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            // check if sum - k in hash
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            // push sum into hash
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}
