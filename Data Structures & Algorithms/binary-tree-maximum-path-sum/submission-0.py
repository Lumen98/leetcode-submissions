# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # in order traversal --> returned the list of nodes
        # returned the largest window
        self.res = float("-inf")
        
        def postOrder(curr):
            if not curr:
                return 0
            

            left = max(0, postOrder(curr.left))
            right = max(0, postOrder(curr.right))

            self.res = max(self.res, curr.val + left + right)

            return curr.val + max(left, right)

        postOrder(root)

        return self.res
