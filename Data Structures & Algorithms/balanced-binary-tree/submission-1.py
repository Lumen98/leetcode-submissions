# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, depth):
            if not node:
                return [True, 0]
            
            leftDepth = dfs(node.left, depth + 1)
            rightDepth = dfs(node.right, depth + 1)
            
            balanced = leftDepth[0] and rightDepth[0] and abs(leftDepth[1] - rightDepth[1]) <= 1
            
            return [balanced, 1 + max(leftDepth[1], rightDepth[1])]
        
        return dfs(root, 0)[0]