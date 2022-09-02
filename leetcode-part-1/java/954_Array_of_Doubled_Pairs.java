class Solution {
    public boolean canReorderDoubled(int[] A) {
        HashMap<Integer, Integer> valueMap = new HashMap<>();
        // Sort in[] with comparator
        A = Arrays.stream(A).
                boxed().
                sorted((a, b) -> Integer.compare(Math.abs(a), Math.abs(b))).
                mapToInt(i -> i).
                toArray();
        for (int n: A) valueMap.put(n, valueMap.getOrDefault(n, 0) + 1);
        for (int n: A) {
            if (valueMap.get(n) <= 0) continue;
            if (valueMap.containsKey(2 * n) && valueMap.get(2 * n) > 0) {
                valueMap.put(n, valueMap.get(n) - 1);
                valueMap.put(2 * n, valueMap.get(2 * n) - 1);
            } else {
                return false;
            }
        }
        return true;
    }


}
