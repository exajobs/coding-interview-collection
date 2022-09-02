class Solution {
    /*public boolean backspaceCompare(String S, String T) {
        // https://leetcode.com/problems/backspace-string-compare/discuss/135603/C%2B%2BJavaPython-O(N)-time-and-O(1)-space
        int i = S.length() - 1, j = T.length() - 1;
        while (true) {
            for (int back = 0; i >= 0 && (back > 0 || S.charAt(i) == '#'); --i)
                back += S.charAt(i) == '#' ? 1 : -1;
            for (int back = 0; j >= 0 && (back > 0 || T.charAt(j) == '#'); --j)
                back += T.charAt(j) == '#' ? 1 : -1;
            if (i >= 0 && j >= 0 && S.charAt(i) == T.charAt(j)) {
                i--; j--;
            } else
                return i == -1 && j == -1;
        }
    }*/

    public boolean backspaceCompare(String S, String T) {
        return trans(S).equals(trans(T));
    }
    private String trans(String str) {
        StringBuilder sb = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (c != '#') { sb.append(c); } // if not '#', append it at the end of sb.
            else if (sb.length() > 0) { sb.deleteCharAt(sb.length() - 1); } // remove last char in sb, if sb is not empty.
        }
        return sb.toString();
    }

}
