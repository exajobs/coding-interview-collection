class KthLargest {

    final PriorityQueue<Integer> q;
    final int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        q = new PriorityQueue<>(k);
        // remove n - k smallest number
        for (int val : nums)
            add(val);
    }

    public int add(int val) {
        // add to heaq if it's less then k
        if (q.size() < k)
            q.offer(val);
        else if (q.peek() < val) {
            // if len(heaq) == k, and val greater than smallest num
            // then pop smallest num than add val to heap
            q.poll();
            q.offer(val);
        }
        return q.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */