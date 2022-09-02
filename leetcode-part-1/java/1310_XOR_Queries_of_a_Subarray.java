class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] res = new int[queries.length], q;
        // Compute accumulated xor from head
        for (int i = 1; i < arr.length; i++)
            arr[i] ^= arr[i - 1];
        // query result equals to xor[0, l] xor xor[0, r]
        for (int i = 0; i < queries.length; i++) {
            q = queries[i];
            res[i] = q[0] > 0 ? arr[q[0] - 1] ^ arr[q[1]] : arr[q[1]];
        }
        return res;
    }
}
