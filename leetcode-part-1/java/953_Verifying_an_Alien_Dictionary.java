class Solution {
    HashMap<Character, Integer> orderMap = new HashMap<>();
    public boolean isAlienSorted(String[] words, String order) {
        // Put value index map into hashmap
        for (int i = 0; i < order.length(); i++) {
            orderMap.put(order.charAt(i), i);
        }
        for (int i = 0; i < words.length - 1; i++) {
            if (cmp_alien(words[i], words[i + 1]) > 0) return false; 
        }
        return true;
        
    }
    private int cmp_alien(String a, String b) {
        int ls = a.length() < b.length() ? a.length(): b.length();
        int pos = 0;
        // Compare based on hashmap
        while (pos < ls) {
            if (orderMap.get(a.charAt(pos)) != orderMap.get(b.charAt(pos)))
                return orderMap.get(a.charAt(pos)) - orderMap.get(b.charAt(pos));
            pos += 1;
        }
        return a.length() <= b.length() ? -1: 1;
    }
}
