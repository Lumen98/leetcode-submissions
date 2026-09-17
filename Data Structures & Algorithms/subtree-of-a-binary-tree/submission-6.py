# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            queue = deque([(p, q)])

            while queue:
                left, right = queue.popleft()

                if not left and not right:
                    continue
                if not left or not right:
                    return False
                if left.val != right.val:
                    return False
                
                queue.append((left.left, right.left))
                queue.append((left.right, right.right))
            
            return True
        

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr.val == subRoot.val:
                if isSame(curr, subRoot):
                    return True
            
            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)
        
        return False



