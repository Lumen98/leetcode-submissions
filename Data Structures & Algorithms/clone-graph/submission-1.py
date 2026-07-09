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
            return None

        # dfs through the graph
        # at each node, create a brand new node
        # map oldNode : newNode
        # loop through that map and add neighbors

        stack = [node]
        visited = set()
        
        hashmap = {}

        while stack:
            curr = stack.pop(-1)

            if curr in visited:
                continue
            visited.add(curr)

            newNode = Node(curr.val)

            hashmap[curr] = newNode
        
            for nei in curr.neighbors:
                stack.append(nei)
        

        for old, new in hashmap.items():
            for oldNei in old.neighbors:
                new.neighbors.append(hashmap[oldNei])
        
        return hashmap[node]




        