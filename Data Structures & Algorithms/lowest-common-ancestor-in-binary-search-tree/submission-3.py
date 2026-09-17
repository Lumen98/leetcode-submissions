# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        iterator = root
        while iterator:
            if p.val == iterator.val or q.val == iterator.val:
                return iterator
            elif p.val < iterator.val and q.val < iterator.val:
                iterator = iterator.left
            elif p.val > iterator.val and q.val > iterator.val:
                iterator = iterator.right
            else:
                return iterator
        
        return root
            
            


