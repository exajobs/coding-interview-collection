class Solution {
    public int[] anagramMappings(int[] A, int[] B) {
        int[] ans = new int[A.length];
        HashMap<Integer, Integer> valIndex = new HashMap<>();
        for (int i = 0; i < B.length; i++) valIndex.put(B[i], i);
        for (int i = 0; i < A.length; i++) ans[i] = valIndex.get(A[i]);
        return ans;
    }
}
