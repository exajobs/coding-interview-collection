class Solution {
    // https://leetcode.com/problems/fruit-into-baskets/solution/
/*    public int totalFruit(int[] tree) {
        // We'll make a list of indexes for which a block starts.
        List<Integer> blockLefts = new ArrayList();

        // Add the left boundary of each block
        for (int i = 0; i < tree.length; ++i)
            if (i == 0 || tree[i-1] != tree[i])
                blockLefts.add(i);

        // Add tree.length as a sentinel for convenience
        blockLefts.add(tree.length);

        int ans = 0, i = 0;
        search: while (true) {
            // We'll start our scan at block[i].
            // types : the different values of tree[i] seen
            // weight : the total number of trees represented
            //          by blocks under consideration
            Set<Integer> types = new HashSet();
            int weight = 0;

            // For each block from the i-th and going forward,
            for (int j = i; j < blockLefts.size() - 1; ++j) {
                // Add each block to consideration
                types.add(tree[blockLefts.get(j)]);
                weight += blockLefts.get(j+1) - blockLefts.get(j);

                // If we have 3+ types, this is an illegal subarray
                if (types.size() >= 3) {
                    i = j - 1;
                    continue search;
                }

                // If it is a legal subarray, record the answer
                ans = Math.max(ans, weight);
            }

            break;
        }

        return ans;
    }*/

    public int totalFruit(int[] tree) {
        int ans = 0, i = 0;
        Counter count = new Counter();
        for (int j = 0; j < tree.length; ++j) {
            count.add(tree[j], 1);
            while (count.size() >= 3) {
                count.add(tree[i], -1);
                if (count.get(tree[i]) == 0)
                    count.remove(tree[i]);
                i++;
            }

            ans = Math.max(ans, j - i + 1);
        }

        return ans;
    }
}

class Counter extends HashMap<Integer, Integer> {
    public int get(int k) {
        return containsKey(k) ? super.get(k) : 0;
    }

    public void add(int k, int v) {
        put(k, get(k) + v);
    }
}
