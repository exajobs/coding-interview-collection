class Solution {
    /*public void dfs(TreeNode root, Set<Integer> uniques) {
        if (root != null) {
            uniques.add(root.val);
            dfs(root.left, uniques);
            dfs(root.right, uniques);
        }
    }
    public int findSecondMinimumValue(TreeNode root) {
        // Brute force
        Set<Integer> uniques = new HashSet<Integer>();
        dfs(root, uniques);

        int min1 = root.val;
        long ans = Long.MAX_VALUE;
        for (int v : uniques) {
            if (min1 < v && v < ans) ans = v;
        }
        return ans < Long.MAX_VALUE ? (int) ans : -1;
    }*/

    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        int min_val = root.val;
        int ans = Integer.MAX_VALUE;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node == null) continue;
            if (node.val < ans && node.val > min_val) {
                ans = node.val;
            } else if (node.val == min_val) {
                stack.push(node.left);
                stack.push(node.right);
            }
        }
        return ans < Integer.MAX_VALUE ? ans : -1;
    }
}
