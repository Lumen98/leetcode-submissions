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
        
        hashmap = {} # old node to new node

        queue = deque([node])
        visited = set()

        while queue:
            curr = queue.popleft()

            new = Node(curr.val, None)

            hashmap[curr] = new

            for nei in curr.neighbors:
                if nei in visited:
                    continue
                queue.append(nei)
                visited.add(nei)
        
        for old in hashmap:
            for nei in old.neighbors:
                hashmap[old].neighbors.append(hashmap[nei])


        return hashmap[node]






