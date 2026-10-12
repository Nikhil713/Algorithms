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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode* fastNode = &dummy;
        ListNode* slowNode = &dummy;
        int i = 0;

        for(i = 0; i<= n; i++){
            fastNode = fastNode -> next;
        }
        while(fastNode != nullptr){
            fastNode = fastNode-> next;
            slowNode = slowNode-> next;
        }
        slowNode-> next = slowNode->next->next;
        return dummy.next;
    }
};


// // My approach

// /**
//  * Definition for singly-linked list.
//  * struct ListNode {
//  *     int val;
//  *     ListNode *next;
//  *     ListNode() : val(0), next(nullptr) {}
//  *     ListNode(int x) : val(x), next(nullptr) {}
//  *     ListNode(int x, ListNode *next) : val(x), next(next) {}
//  * };
//  */
// class Solution {
// public:
//     ListNode* removeNthFromEnd(ListNode* head, int n) {
//         ListNode dummy(0, head);
//         ListNode* prevNode = &dummy;
//         ListNode* counter = head;
//         int i = 0;
//         int count = 0;
//         while(counter != nullptr){
//             counter = counter -> next;
//             count++;
//         }

//         for(i = 0; i< count -n; i++){
//             prevNode = prevNode -> next;
//         }
//         prevNode-> next = prevNode->next->next;
//         return dummy.next;
//     }
// };