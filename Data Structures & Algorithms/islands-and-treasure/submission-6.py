from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        R = len(grid)
        C = len(grid[0])
        queue = deque()
        visited = set()

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            r, c, dist = queue.popleft()
            

            if r + 1 < R and grid[r + 1][c] != -1 and grid[r + 1][c] != 0 and (r + 1, c) not in visited:
                grid[r + 1][c] = dist + 1
                queue.append((r + 1, c, dist + 1)) 
                visited.add((r + 1, c))
            if r - 1 >= 0 and grid[r - 1][c] != -1 and grid[r - 1][c] != 0 and (r - 1, c) not in visited:
                grid[r - 1][c] = dist + 1
                queue.append((r - 1, c, dist + 1))
                visited.add((r - 1, c))
            if c + 1 < C and grid[r][c + 1] != -1 and grid[r][c + 1] != 0 and (r, c + 1) not in visited:
                grid[r][c + 1] = dist + 1
                queue.append((r, c + 1, dist + 1))
                visited.add((r, c + 1))
            if c - 1 >= 0 and grid[r][c - 1] != -1 and grid[r][c - 1] != 0 and (r, c - 1) not in visited:
                grid[r][c - 1] = dist + 1
                queue.append((r, c - 1, dist + 1))
                visited.add((r, c - 1))

