/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    // https://leetcode.com/problems/subtree-of-another-tree/solution/
    HashSet < String > trees = new HashSet < > ();
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String tree1 = preorder(s, true);
        String tree2 = preorder(t, true);
        return tree1.indexOf(tree2) >= 0;
    }
    public String preorder(TreeNode t, boolean left) {
        if (t == null) {
            if (left)
                return "lnull";
            else
                return "rnull";
        }
        return "#"+t.val + " " +preorder(t.left, true)+" " +preorder(t.right, false);
    }

    // public boolean isSubtree(TreeNode s, TreeNode t) {
    //     return traverse(s,t);
    // }
    // public boolean equals(TreeNode x,TreeNode y)
    // {
    //     if(x==null && y==null)
    //         return true;
    //     if(x==null || y==null)
    //         return false;
    //     return x.val==y.val && equals(x.left,y.left) && equals(x.right,y.right);
    // }
    // public boolean traverse(TreeNode s,TreeNode t)
    // {
    //     return  s!=null && ( equals(s,t) || traverse(s.left,t) || traverse(s.right,t));
    // }
}
