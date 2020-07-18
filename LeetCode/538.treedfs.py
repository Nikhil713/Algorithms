# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# Example:

# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13

# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.temp = 0
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.temp+= node.val
            node.val = self.temp
            dfs(node.left)
        
        dfs(root)
        return root