# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import heapq
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root.left and not root.right:
            return 1
        
        res = 0
         
        q = deque([(root, root.val)])


        while q:
            curr, maxSoFar = q.popleft()

            if curr.val >= maxSoFar:
                res += 1
            
            maxSoFar = max(curr.val, maxSoFar)

            if curr.left:
                q.append((curr.left, maxSoFar))
        
            if curr.right:
                q.append((curr.right, maxSoFar))

        return res



















