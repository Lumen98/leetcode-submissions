class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        self.R = len(heights)
        self.C = len(heights[0])

        for r in range(self.R):
            for c in range(self.C):
                if self.dfs(r, c, heights, checkingPacific=True) and \
                   self.dfs(r, c, heights, checkingPacific=False):
                    res.append([r, c])

        return res

    def dfs(self, row, col, grid, checkingPacific: bool) -> bool:
        stack = [(row, col)]
        visited = set()

        while stack:
            r, c = stack.pop(-1)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # reached desired ocean?
            if checkingPacific:
                if self.checkPacific(r, c):
                    return True
            else:
                if self.checkAtlantic(r, c):
                    return True

            curVal = grid[r][c]

            if r + 1 < self.R and grid[r + 1][c] <= curVal:
                stack.append((r + 1, c))
            if r - 1 >= 0 and grid[r - 1][c] <= curVal:
                stack.append((r - 1, c))
            if c + 1 < self.C and grid[r][c + 1] <= curVal:  # fixed bound
                stack.append((r, c + 1))
            if c - 1 >= 0 and grid[r][c - 1] <= curVal:
                stack.append((r, c - 1))
        
        return False

    def checkPacific(self, r, c): 
        if r == 0: 
            return True 
        if c == 0: 
            return True 
        return False

    def checkAtlantic(self, r, c): 
        if r == self.R - 1: 
            return True 
        if c == self.C - 1: 
            return True 
        
        return False

















