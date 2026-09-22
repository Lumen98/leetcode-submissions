class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        
        pacific = set() # rows (0,0) -> (R - 1, 0) and (0, 0) -> (0, C - 1)
        atlantic = set() # (0, C - 1) -> (R - 1, C - 1)  and (R - 1, 0) -> (R - 1, C - 1)

        for r in range(R):
            pacific.add((r, 0))
            atlantic.add((r, C - 1))
        for c in range(C):
            pacific.add((0, c))
            atlantic.add((R - 1, c))

        def bfs(queue):
            visited = set()
            while queue:
                r, c = queue.popleft()

                if (r, c) in visited:
                    continue
                
                visited.add((r, c))

                if r + 1 < R and heights[r + 1][c] >= heights[r][c]:
                    queue.append((r + 1, c))
                if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                    queue.append((r - 1, c))
                if c + 1 < C and heights[r][c + 1] >= heights[r][c]:
                    queue.append((r, c + 1))
                if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                    queue.append((r, c - 1))

            return visited
        
        # pacific 
        queueP = deque(pacific)
        pacific = bfs(queueP)
        del queueP

        # atlantic
        queueA = deque(atlantic)
        atlantic = bfs(queueA)
        del queueA

        res = []

        for (r, c) in pacific & atlantic:
            res.append([r, c])
        
        return res


