# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        node = root
        while stack or node:
            # go left as far as possible
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()      # visit in ascending order
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return 0  # fallback; constraints usually guarantee k is valid

        
            




        



        