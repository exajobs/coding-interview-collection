import java.util.Stack;

import javax.swing.tree.TreeNode;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    /* public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) return 0;
        if (root.left != null
            && root.left.left == null
            && root.left.right == null)
            return root.left.val + sumOfLeftLeaves(root.right);
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
    } */

    public int sumOfLeftLeaves(TreeNode root) {
        int res = 0;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node != null) {
                if (node.left != null
                    && node.left.left == null
                    && node.left.right == null)
                    res += node.left.val;
                stack.push(node.right);
                stack.push(node.left);
            }
        }
        return res;
    }
}
