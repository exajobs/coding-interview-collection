class Solution {
/*    public int[] sortArrayByParity(int[] A) {
        A = Arrays.stream(A).
                boxed().
                sorted((a, b) -> Integer.compare(a% 2, b % 2)).
                mapToInt(i -> i).
                toArray();
        return A;
    }*/

    /*public int[] sortArrayByParity(int[] A) {
        int[] ans = new int[A.length];
        int pos = 0;
        for (int num: A) 
            if (num % 2 == 0)
                ans[pos++] = num;
        for (int num: A) 
            if (num % 2 == 1)
                ans[pos++] = num;
        return ans;
    }*/

    public int[] sortArrayByParity(int[] A) {
        int lo = 0, hi = A.length - 1;
        while (lo < hi) {
            if (A[lo] % 2 > A[hi] % 2) {
                int tmp = A[hi];
                A[hi] = A[lo];
                A[lo] = tmp;
            }
            if (A[lo] % 2 == 0) lo++;
            if (A[hi] % 2 == 1) hi--;
        }
        return A;
    }
}
