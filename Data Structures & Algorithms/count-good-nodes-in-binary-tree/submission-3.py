# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        stack = [(root, float("-inf"))]

        goodNodes = 0

        while stack:
            curr, currMax = stack.pop(-1)

            if currMax <= curr.val:
                goodNodes += 1
            currMax = max(curr.val, currMax)

            
            if curr.left:
                stack.append((curr.left, currMax))
            if curr.right:
                stack.append((curr.right, currMax))


        return goodNodes

