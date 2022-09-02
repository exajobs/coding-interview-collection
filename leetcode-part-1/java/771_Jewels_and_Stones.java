import java.util.HashSet;

class Solution {
    public int numJewelsInStones(String J, String S) {
        int result = 0;
        HashSet jHash = new HashSet<>();
        for (int j = 0; j < J.length(); j++) {
            jHash.add(J.charAt(j));
        }
        for (int s = 0; s < S.length(); s++) {
            if (jHash.contains(S.charAt(s))) {
                result++;
            }
        }
        return result;
    }
}
