class Solution {
    /* public int[] sortedSquares(int[] A) {
        int[] res = new int[A.length];
        for (int i = 0; i < A.length; ++i)
            res[i] = A[i] * A[i];

        Arrays.sort(res);
        return res;
    } */
    public int[] sortedSquares(int[] A) {
        int pos = 0;
        int[] res = new int[A.length];
        int curr = 0;
        while (pos < A.length && A[pos] < 0) pos++;
        int npos = pos - 1;
        while (pos < A.length && npos >= 0) {
            if (A[pos] * A[pos] < A[npos] * A[npos]) {
                res[curr++] = A[pos] * A[pos];
                pos++;
            } else {
                res[curr++] = A[npos] * A[npos];
                npos--;
            }
        }
        while (npos >= 0) {
            res[curr++] = A[npos] * A[npos];
            npos--;
        }
        while (pos < A.length) {
            res[curr++] = A[pos] * A[pos];
            pos++;
        }
        return res;
    }
}
