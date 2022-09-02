class Solution {
    public int repeatedNTimes(int[] A) {
        HashMap<Integer, Integer> hash = new HashMap<>();
        int ans = A[0];
        for (int n: A) {
            int count = hash.getOrDefault(n, 0) + 1;
            hash.put(n, count);
            if (count >= hash.get(ans)) ans = n;
        }
        return ans;
    }
}
