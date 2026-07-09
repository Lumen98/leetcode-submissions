"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = set()
        stack = [node]
        hashmap = {}


        while stack:
            curr = stack.pop(-1)
            if curr in visited:
                continue
            visited.add(curr)
            newNode = Node(curr.val)
            hashmap[curr] = newNode

            for n in curr.neighbors:
                stack.append(n)


        for old, new in hashmap.items():
            for n in old.neighbors:
                new.neighbors.append(hashmap[n])


        return hashmap[node]