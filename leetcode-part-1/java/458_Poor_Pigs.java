class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int n = minutesToTest / minutesToDie + 1;
        int pigs = 0;
        while (Math.pow(n, pigs) < buckets) pigs++;
        return pigs; 
    }
}
