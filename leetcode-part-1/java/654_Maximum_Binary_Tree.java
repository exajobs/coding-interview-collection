public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length);
    }
    public TreeNode construct(int[] nums, int l, int r) {
        if (l == r)
            return null;
        int max_i = max(nums, l, r);
        TreeNode root = new TreeNode(nums[max_i]);
        root.left = construct(nums, l, max_i);
        root.right = construct(nums, max_i + 1, r);
        return root;
    }
    public int max(int[] nums, int l, int r) {
        int max_i = l;
        for (int i = l; i < r; i++) {
            if (nums[max_i] < nums[i])
                max_i = i;
        }
        return max_i;
    }
    /*public TreeNode constructMaximumBinaryTree(int[] nums) {
        // https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C++-O(N)-solution
        Stack<TreeNode> stack = new Stack<>();
        for (int i=0; i<nums.length(); i++) {
            TreeNode curr = new TreeNode(nums[i]);
            while (!stack.empty() && stack.peek().val < nums[i]) {
                curr.left = stack.pop();
            }
            if (!stack.empty()) 
                stack.peek().right = curr;
            stack.push(curr);
        }
        while (stack.size() != 1) {
            stack.pop()
        }
        return stack.peek();
    }*/
}
