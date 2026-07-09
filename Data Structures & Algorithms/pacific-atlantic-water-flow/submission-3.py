class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R = len(heights)
        C = len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visited):
            stack = [(row, col)]

            while stack:
                r, c = stack.pop(-1)
                if ((r, c)) in visited:
                    continue
                visited.add((r, c))
                
                if r + 1 < R and heights[r + 1][c] >= heights[r][c]:
                    stack.append((r + 1, c))
                if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                    stack.append((r - 1, c))
                if c + 1 < C and heights[r][c + 1] >= heights[r][c]:
                    stack.append((r, c + 1))
                if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                    stack.append((r, c - 1))

        for c in range(C):
            dfs(0, c, pac)
            dfs(R - 1, c, atl)
        for r in range(R):
            dfs(r, 0, pac)
            dfs(r, C - 1, atl)

        res = []
        for r in range(R):
            for c in range(C):
                if ((r, c)) in pac and ((r, c)) in atl:
                    res.append([r, c])

        return res


