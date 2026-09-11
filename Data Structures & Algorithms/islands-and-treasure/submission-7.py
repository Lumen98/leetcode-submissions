class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None 

        R = len(grid)
        C = len(grid[0])
        queue = collections.deque()
        visited = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, currDist = queue.popleft()

            if r + 1 < R and grid[r + 1][c] != -1 and grid[r + 1][c] != 0 and (r + 1, c) not in visited:
                visited.add((r + 1, c))
                grid[r + 1][c] = currDist + 1
                queue.append((r + 1, c, currDist + 1))
            if r - 1 >= 0 and grid[r - 1][c] != -1 and grid[r - 1][c] != 0 and (r - 1, c) not in visited:
                visited.add((r - 1, c))
                grid[r - 1][c] = currDist + 1
                queue.append((r - 1, c, currDist + 1))
            if c + 1 < C and grid[r][c + 1] != -1 and grid[r][c + 1] != 0 and (r, c + 1) not in visited:
                visited.add((r, c + 1))
                grid[r][c + 1] = currDist + 1
                queue.append((r, c + 1, currDist + 1))
            if c - 1 >= 0 and grid[r][c - 1] != -1 and grid[r][c - 1] != 0 and (r, c - 1) not in visited: 
                visited.add((r, c - 1))
                grid[r][c - 1] = currDist + 1
                queue.append((r, c - 1, currDist + 1))

        




