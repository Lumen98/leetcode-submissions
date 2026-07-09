# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = [(root, float("-inf"))]

        good = 0

        while stack:
            curr, path = stack.pop(-1)

            if curr.val >= path:
                good += 1
                path = curr.val
                
            if curr.left:
                stack.append((curr.left, path))
            if curr.right:
                stack.append((curr.right, path))
        
        return good

