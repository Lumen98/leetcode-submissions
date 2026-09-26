from collections import deque 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if (n - 1) != len(edges):
            return False

        graph = {}
        
        for i in range(n):
            graph[i] = []

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        queue = deque([(0, -1)])
        visited = set() 

        while queue:
            curr, parent = queue.popleft()

            if curr in visited:
                continue
            
            visited.add(curr)

            for nei in graph[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                queue.append((nei, curr))

        return len(visited) == n


