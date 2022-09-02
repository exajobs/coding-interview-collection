class Solution {
    /* public int fixedPoint(int[] A) {
        for (int i = 0; i < A.length; i++) {
            // Because if A[i] > i, then i can never be greater than A[i] any more
            if (A[i] == i) return i;
            else if (A[i] > i) return -1;
        }
        return -1;
    } */
    public int fixedPoint(int[] A) {
        int l = 0;
        int h = A.length;
        while (l <= h) {
            int mid = (l + h) / 2;
            if (A[mid] > mid) h = mid - 1;
            else if (A[mid] < mid) l = mid + 1;
            else return mid;
        }
        return -1;
    }
}
