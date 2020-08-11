// Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

// Return the decimal value of the number in the linked list.

 

// Example 1:

// Input: head = [1,0,1]
// Output: 5
// Explanation: (101) in base 2 = (5) in base 10

// Example 2:

// Input: head = [0]
// Output: 0

// Example 3:

// Input: head = [1]
// Output: 1

// Example 4:

// Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
// Output: 18880

// Example 5:

// Input: head = [0,0]
// Output: 0

 

// Constraints:

//     The Linked List is not empty.
//     Number of nodes will not exceed 30.
//     Each node's value is either 0 or 1.

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
    int getDecimalValue(ListNode* head) {
        vector<int> res;
        while(head){
            res.push_back(head->val);
            head = head ->next;
        }
        int finalres = 0;
        reverse(res.begin(),res.end());
        for(auto i = 0;i < res.size();i++){
            if(res[i] == 1){
                finalres = finalres + pow(2,i);
            }
        }
        return finalres;
    }
};