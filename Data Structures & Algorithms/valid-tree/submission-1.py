class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        graph = {}
        
        for i in range(n):
            graph[i] = []

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        start = True
        stack = [(0, -1)]

        while stack:
            curr, prev = stack.pop(-1)

            if curr in visited:
                continue
            visited.add(curr)

            for nei in graph[curr]:
                if nei == prev:
                    continue
                if nei in visited:
                    return False
                stack.append((nei, curr))

        return len(visited) == n









