class Solution {
    public char findTheDifference(String s, String t) {
        int total = t.charAt(s.length());
        for (int i = 0; i < s.length(); i++)
            total += (t.charAt(i) - s.charAt(i));
        return (char) total;
    }

    /* public char findTheDifference(String s, String t) {
        int total = t.charAt(s.length());
        for (int i = 0; i < s.length(); i++) {
            total ^= t.charAt(i);
            total ^= s.charAt(i);
        }
        return (char) total;
    } */
}
