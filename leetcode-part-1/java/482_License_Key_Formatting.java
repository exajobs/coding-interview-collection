class Solution {
    public String licenseKeyFormatting(String s, int k) {
        // https://leetcode.com/problems/license-key-formatting/discuss/96512/Java-5-lines-clean-solution
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--)
            if (s.charAt(i) != '-')
                sb.append(sb.length() % (k + 1) == k ? '-' : "").append(s.charAt(i));
        return sb.reverse().toString().toUpperCase();
    } 
}
