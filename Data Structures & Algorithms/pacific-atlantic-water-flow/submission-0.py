class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        self.R = len(heights)
        self.C = len(heights[0])

        for r in range(self.R):
            for c in range(self.C):
                if self.dfs_to_border(r, c, heights, pacific=True) and \
                   self.dfs_to_border(r, c, heights, pacific=False):
                    res.append([r, c])

        return res

    def dfs_to_border(self, row, col, grid, pacific: bool) -> bool:
        """Downhill/flat DFS from (row,col) to a target border."""
        stack = [(row, col)]
        visited = set()

        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # reached desired ocean?
            if pacific:
                if r == 0 or c == 0:
                    return True
            else:
                if r == self.R - 1 or c == self.C - 1:
                    return True

            h = grid[r][c]
            if r + 1 < self.R and grid[r + 1][c] <= h:
                stack.append((r + 1, c))
            if r - 1 >= 0 and grid[r - 1][c] <= h:
                stack.append((r - 1, c))
            if c + 1 < self.C and grid[r][c + 1] <= h:  # fixed bound
                stack.append((r, c + 1))
            if c - 1 >= 0 and grid[r][c - 1] <= h:
                stack.append((r, c - 1))

        return False

















