class Solution {
    /*public int fib(int N) {
        // Recursively, O(n)
        if (N == 0) return 0;
        if (N == 1) return 1;
        return fib(N - 1) + fib(N - 2);
    }*/

    private List<Integer> memo;

    public Solution() {
        memo = new ArrayList();
        memo.add(0);
        memo.add(1);
    }

    public int fib(int N) {
        // Dp with memo, O(n)
        if (N < memo.size()) return memo.get(N);
        for (int i = memo.size(); i <= N; i++) {
            memo.add(memo.get(i - 1) + memo.get(i - 2));
        }
        return memo.get(N);
    }
}
