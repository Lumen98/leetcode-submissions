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

        stack = [(0, -1)]
        visited = set()

        while stack:
            curr, parent = stack.pop(-1)
            if curr in visited:
                continue

            visited.add(curr)

            for nei in graph[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                stack.append((nei, curr))

        return True


