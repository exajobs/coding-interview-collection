import java.util.HashMap;

public class NR {
    public static void main(String[] args) {
        // NOTE: The following input values will be used for testing your solution.
        nonRepeating("abcab"); // should return 'c'
        nonRepeating("abab"); // should return null
        nonRepeating("aabbbc"); // should return 'c'
        nonRepeating("aabbdbc"); // should return 'd'
    }

    // Implement your solution below.
    public static Character nonRepeating(String s) {
        HashMap<Character, Integer> charCount = new HashMap<Character, Integer>();
        // NOTE: Using s.toCharArray() is no the most efficient method,
        // but I chose to use it here for simplicity.
        for (char c : s.toCharArray()) {
            if (charCount.containsKey(c)) {
                Integer newVal = charCount.get(c) + 1;
                charCount.put(c, newVal);
            } else {
                charCount.put(c, 1);
            }
        }
        for (char c : s.toCharArray()) {
            if (charCount.get(c) == 1) return c;
        }
        return null;
    }
}
