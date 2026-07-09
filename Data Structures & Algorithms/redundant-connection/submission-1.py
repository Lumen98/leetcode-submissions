from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        graph = defaultdict(list)

        def dfs(node, parent):
            stack = [(node, parent)]

            while stack:
                curr, parent = stack.pop(-1)

                if visit[curr]:
                    return True
                visit[curr] = True
            
                for nei in graph[curr]:
                    if nei == parent:
                        continue
                    stack.append((nei, curr))
            
            return False

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
            visit = [False] * (n + 1)

            if dfs(n1, -1):
                return [n1, n2]
        return []







