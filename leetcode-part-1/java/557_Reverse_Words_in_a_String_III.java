public class Solution {
    public String reverseWords(String s) {
        String words[] = s.split(" ");
        StringBuilder ans = new StringBuilder();
        for (String word: words)
            ans.append(new StringBuffer(word).reverse().toString() + " ");
        return ans.toString().trim();
    }
}
