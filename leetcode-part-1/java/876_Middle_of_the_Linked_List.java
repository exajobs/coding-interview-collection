/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // public ListNode middleNode(ListNode head) {
    //     List<ListNode> array = new ArrayList<ListNode>();
    //     while (head != null) {
    //         array.add(head);
    //         head = head.next;
    //     }
    //     return array.get(array.size() / 2);
    // }
    public ListNode middleNode(ListNode head) {
        ListNode fast, slow;
        fast = slow = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
