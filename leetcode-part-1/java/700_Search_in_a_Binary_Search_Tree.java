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
    /*public TreeNode searchBST(TreeNode root, int val) {
        // Recursive
        if (root == null) return root;
        if (root.val == val) return root;
        else return val<root.val? searchBST(root.left,val):searchBST(root.right,val);
    }*/
    public TreeNode searchBST(TreeNode root, int val) {
        // Iteration
        while(root != null && root.val != val) {
            root = val < root.val ? root.left: root.right;
        }
        return root;
    }
}
