import java.util.Map;

class Solution {
/*     public int[] smallerNumbersThanCurrent(int[] nums) {
        Map<Integer, Integer> sortedIndex = new HashMap<>();
        int[] sortedNums = new int[nums.length];
        // sort and get position
        System.arraycopy(nums, 0, sortedNums, 0, nums.length);
        Arrays.sort(sortedNums);
        for (int i = 0; i < nums.length; i++) {
            if (sortedIndex.containsKey(sortedNums[i])) continue;
            sortedIndex.put(sortedNums[i], i);
        }
        for (int i = 0; i < nums.length; i++)
            sortedNums[i] = sortedIndex.get(nums[i]);
        return sortedNums;
    } */

    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] countList = new int[101];
        int[] res = new int[nums.length];
        // count numbers
        for (int i = 0; i < nums.length; i++)
            countList[nums[i]]++;
        // compute numbers before current index
        for (int i = 1; i < 101; i++)
            countList[i] += countList[i-1];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) res[i] = 0;
            else res[i] = countList[nums[i]-1];
        }
        return res;
    }
}
