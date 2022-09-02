class Solution {
    /*public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // Check position
        return !(rec1[2] <= rec2[0] ||   // left
                 rec1[3] <= rec2[1] ||   // bottom
                 rec1[0] >= rec2[2] ||   // right
                 rec1[1] >= rec2[3]);    // top
    }*/
    /*public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // Check area
        // https://leetcode.com/problems/rectangle-area/discuss/62149/Just-another-short-way
        int left = Math.max(rec1[0], rec2[0]), right = Math.max(Math.min(rec1[2], rec2[2]), left);
        int bottom = Math.max(rec1[1], rec2[1]), top = Math.max(Math.min(rec1[3], rec2[3]), bottom);
        return (right - left) * (top - bottom) != 0;
    }*/

    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // Check area
        return (Math.min(rec1[2], rec2[2]) > Math.max(rec1[0], rec2[0]) && // width > 0
                Math.min(rec1[3], rec2[3]) > Math.max(rec1[1], rec2[1]));  // height > 0
    }
}