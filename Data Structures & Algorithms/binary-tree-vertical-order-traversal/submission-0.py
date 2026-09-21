# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        
        cols = defaultdict(list)

        minCol = 0
        maxCol = 0

        while queue:
            curr, col = queue.popleft()

            cols[(col)].append(curr.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if curr.left:
                queue.append((curr.left, col - 1))
            
            if curr.right:
                queue.append((curr.right, col + 1))

        
        return [cols[c] for c in range(minCol, maxCol + 1)]

