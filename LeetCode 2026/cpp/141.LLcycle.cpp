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
    bool hasCycle(ListNode *head) {
        ListNode* head1 = head;
        ListNode* head2 = head;
        while(head2 != nullptr && head2->next != nullptr){
            head1 = head1->next;
            head2 = head2->next->next;
            if(head1 == head2){
                return true;
            }
        }
        return false;
    }
};