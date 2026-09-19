# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        queue = deque([(root, 0)])

        res = []
        prevLevel = -1

        while queue:
            curr, level = queue.popleft()

            if curr.left:
                queue.append((curr.left, level + 1))

            if curr.right:
                queue.append((curr.right, level + 1))

            if queue and queue[0][1] > level:
                res.append(curr.val)
            if not queue:
                res.append(curr.val)

        return res





