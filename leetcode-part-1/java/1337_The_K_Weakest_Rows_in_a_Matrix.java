class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        List<Integer> res = new ArrayList<>();
        int col = 0;
        boolean flag = true;
        while (col < mat[0].length && flag) {
            for (int i = 0; i < mat.length; i++) {
                if (res.contains(i)) continue;
                // Add first row with 0 into res
                if (mat[i][col] == 0) res.add(i);
                if (res.size() == k) {
                    flag = false;
                    break;
                }
            }
            col += 1;
        }
        if (flag) {
            // if res less than k
            for (int i = 0; i < mat.length; i++) {
                if (res.contains(i)) continue;
                res.add(i);
                if (res.size() == k) break;
            }
        }
        int[] ret = new int[k];
        for (int i = 0; i < k; i++) ret[i] = res.get(i);
        return ret;
    }
}
