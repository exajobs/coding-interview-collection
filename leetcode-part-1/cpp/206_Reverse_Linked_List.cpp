/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        if (head == NULL)
            return NULL;
        if (head->next == NULL)
            return head;
        // Previous pointer
        ListNode *previous = head;
        // Current pointer
        ListNode *curr = head->next;
        head->next = NULL;
        while (curr->next) {
            ListNode *next = curr->next;
            curr->next = previous;
            previous = curr;
            curr = next;
        }
        curr->next = previous;
        return curr;
    }
};
