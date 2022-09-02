class Solution {
    // https://leetcode.com/problems/convert-bst-to-greater-tree/solution/
    // private int sum = 0;

    // public TreeNode convertBST(TreeNode root) {
    //     if (root != null) {
    //         convertBST(root.right);
    //         sum += root.val;
    //         root.val = sum;
    //         convertBST(root.left);
    //     }
    //     return root;
    // }
    
    public TreeNode convertBST(TreeNode root) {
        int sum = 0;
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<TreeNode>();

        while (!stack.isEmpty() || node != null) {
            /* push all nodes up to (and including) this subtree's maximum on
             * the stack. */
            while (node != null) {
                stack.add(node);
                node = node.right;
            }

            node = stack.pop();
            sum += node.val;
            node.val = sum;

            /* all nodes with values between the current and its parent lie in
             * the left subtree. */
            node = node.left;
        }

        return root;
    }
}
