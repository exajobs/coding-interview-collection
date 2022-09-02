class Solution {
    public int minIncrementForUnique(int[] A) {
        if (A.length == 0) return 0;
        HashSet<Integer> numSet = new HashSet<>();
        List<Integer> duplicated = new ArrayList<>();
        int res = 0;
        Arrays.sort(A);
        int left  = A[0];
        int right = A[A.length - 1];
        int holes = right - left + 1;
        for (int v: A) {
            if (numSet.contains(v)) duplicated.add(v);
            else numSet.add(v);
        }
        holes -= numSet.size();
        for (int i = left + 1; i < right; i++) {
            if (holes == 0 || duplicated.size() == 0) break;
            if (!numSet.contains(i) && i > duplicated.get(0)) {
                res += i - duplicated.get(0);
                holes --;
                duplicated.remove(0);
            }
        }
        if (duplicated.size() == 0) return res;
        while (duplicated.size() != 0) {
            right += 1;
            res += right - duplicated.get(0);
            duplicated.remove(0);
        } 
        return res;
    }
}
