# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        queue = deque([(root, float("-inf"))])
        goodNodes = 0

        while queue:
            curr, currMax = queue.popleft()
            if curr.val >= currMax:
                goodNodes += 1

            currMax = max(currMax, curr.val)

            if curr.left:
                queue.append((curr.left, currMax))
            
            if curr.right:
                queue.append((curr.right, currMax))
        
        return goodNodes 
            
