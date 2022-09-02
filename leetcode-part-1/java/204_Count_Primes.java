class Solution {
    // ttps://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        int count = 0;
        Arrays.fill(isPrime, true);
        for (int i = 2; i < n; i++) {
            if (i * i >= n)
                break;
            if (!isPrime[i])
                continue;
            for (int j = i * i; j < n; j += i)
                isPrime[j] = false;
        }
        for (int i = 2; i < n; i++)
            if (isPrime[i])
                count++;
        return count;
    }
}
