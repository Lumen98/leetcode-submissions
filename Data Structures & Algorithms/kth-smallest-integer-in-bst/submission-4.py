# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        res = 0

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            heapq.heappush(heap, curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        while k > 0: 
            res = heapq.heappop(heap)
            k -= 1

        return res
        
