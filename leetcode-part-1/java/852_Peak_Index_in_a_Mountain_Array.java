class Solution {
    // public int peakIndexInMountainArray(int[] A) {
    //     int i = 0;
    //     for (; A[i] < A[i + 1]; i++);
    //     return i;
    // }

    public int peakIndexInMountainArray(int[] A) {
        int lo = 0, hi = A.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (A[mid] < A[mid + 1]) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
