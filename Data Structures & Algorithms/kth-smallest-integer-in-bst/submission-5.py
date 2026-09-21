# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        nodeCtr = 0


        def dfs(node):
            nonlocal res
            nonlocal nodeCtr
            if not node:
                return 
            
            dfs(node.left)
            nodeCtr += 1
            
            if nodeCtr == k:
                res = node.val
                return


            dfs(node.right)


        dfs(root)

        return res

        
