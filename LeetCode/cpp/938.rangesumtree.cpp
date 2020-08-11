// Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

// The binary search tree is guaranteed to have unique values.

 

// Example 1:

// Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
// Output: 32

// Example 2:

// Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
// Output: 23

 

// Note:

//     The number of nodes in the tree is at most 10000.
//     The final answer is guaranteed to be less than 2^31.


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    void dfs(TreeNode* root,int L, int R){
        if(root){
            // cout<<root ->val<<endl;
            dfs(root -> left,L,R);
            dfs(root -> right,L,R);
            if ((root -> val >= L) && (root -> val <= R)){
                sum+= root -> val;
            }
        }
        return;
    }
    int rangeSumBST(TreeNode* root, int L, int R) {

        dfs(root,L,R);
        return sum;
    }
};