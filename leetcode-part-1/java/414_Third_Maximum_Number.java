public class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(3);
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            if (set.contains(i)) continue;
            pq.offer(i);
            set.add(i);
            if (pq.size() > 3) set.remove(pq.poll());
        }
        while (pq.size() < 3 && pq.size() > 1) {
            pq.poll();
        }
        return pq.peek();
    }
}
