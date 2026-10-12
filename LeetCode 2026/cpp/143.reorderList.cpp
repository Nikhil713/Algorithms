/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode dummy(0,head);
        ListNode* slow = &dummy;
        ListNode* fast= &dummy;

        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second = slow->next;
        slow->next = nullptr;

        ListNode* prev = nullptr;
        ListNode* current = second;
        while(current != nullptr){
            ListNode* nextNode = current->next;
            current->next = prev;
            prev = current;
            current = nextNode;
        }
        second = prev;
        ListNode* first = head;
        ListNode* temp;
        while(second != nullptr){
            temp = first ->next;

            first->next = second;
            second= second->next;
            first->next->next = temp;

            first = temp;
        }
    }
};