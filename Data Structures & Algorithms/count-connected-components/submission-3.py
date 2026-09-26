from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}

        for i in range(n):
            graph[i] = []
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visit = set()
        
        def bfs(node):
            nonlocal visit
            q = deque([node])
            if node not in visit:
                visit.add(node)

            while q:
                cur = q.popleft()
                for nei in graph[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        res = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res += 1

        return res

        
                





