class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        // https://leetcode.com/problems/rectangle-area/discuss/62149/Just-another-short-way
        // Possible overlap area
        int left = Math.max(A, E), right = Math.max(Math.min(C, G), left);
        int bottom = Math.max(B, F), top = Math.max(Math.min(D, H), bottom);
        return (C - A) * (D - B) - (right - left) * (top - bottom) + (G - E) * (H - F);
    }
}
