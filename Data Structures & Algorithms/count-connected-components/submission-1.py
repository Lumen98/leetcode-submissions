class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set()
        
        res = 0

        def dfs(curr):
            if curr in visited:
                return 0
            
            stack = [curr]

            while stack:
                curr = stack.pop(-1)

                if curr in visited:
                    continue
                visited.add(curr)

                for nei in graph[curr]:
                    stack.append(nei)
            return 1
        
        for i in range(n):
            res += dfs(i)
        
        return res







