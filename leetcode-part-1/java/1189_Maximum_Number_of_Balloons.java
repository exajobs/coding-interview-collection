class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (char ch : text.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        int res = Integer.MAX_VALUE;

        res = Math.min(res, map.getOrDefault('b', 0));
        res = Math.min(res, map.getOrDefault('a', 0));
        res = Math.min(res, map.getOrDefault('n', 0));
        res = Math.min(res, map.getOrDefault('l', 0) / 2);
        res = Math.min(res, map.getOrDefault('o', 0) / 2);

        return res;
    }

    /*
    // by @javadev
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[26];
        for (char c : text.toCharArray()) {
            counts[c - 'a']++;
        }
        return Math.min(
                counts[0],
                Math.min(
                        counts[1], Math.min(counts[11] / 2, Math.min(counts[14] / 2, counts[13]))));
    }*/
}
