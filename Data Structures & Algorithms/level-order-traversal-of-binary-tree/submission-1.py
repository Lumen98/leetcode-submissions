# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # index = level, element = list of nodes on that level
        res = []
        
        queue = deque([(root, 0)])

        while queue:
            curr, level = queue.popleft()
            if len(res) <= level:
                res.append([curr.val])
            else:
                res[level].append(curr.val)

            if curr.left:
                queue.append((curr.left, level + 1))
            
            if curr.right:
                queue.append((curr.right, level + 1))
        
        return res

        


        