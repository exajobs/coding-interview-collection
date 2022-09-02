class Solution {
    /*public int binaryGap(int n) {
        // Store Indexes
        int[] A = new int[32];
        int t = 0;
        for (int i = 0; i < 32; ++i)
            if (((N >> i) & 1) != 0)
                A[t++] = i;

        int ans = 0;
        for (int i = 0; i < t - 1; ++i)
            ans = Math.max(ans, A[i+1] - A[i]);
        return ans;
    }*/

    public int binaryGap(int N) {
        int last = -1, ans = 0;
        for (int i = 0; i < 32; ++i)
            if (((N >> i) & 1) > 0) {
                // Store max
                if (last >= 0)
                    ans = Math.max(ans, i - last);
                last = i;
            }
        return ans;
    }
}
