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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while(list1 != nullptr && list2 != nullptr){
            int value1 = list1 -> val;
            int value2 = list2 -> val;
            if (value1 <= value2){
                tail -> next = list1;
                list1 = list1 -> next;
            }
            else{
                tail -> next = list2;
                list2 = list2 -> next;
            }
            tail = tail-> next;
        }
        if(list1 != nullptr){
            tail->next = list1;
        }
        else{
            tail->next = list2;
        }
        return dummy.next;
    }
};