from collections import defaultdict, deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # traverse through the matrix
        # call a bfs from each land cell, get the shortest path to nearest treasure chest

        self.R = len(grid)
        self.C = len(grid[0])

        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == -1:
                    continue
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2147483647:
                    count = self.bfs(r,c, grid)
                    if count > 0:
                        grid[r][c] = count

    def bfs(self, r, c, grid):
        queue = deque(([(r, c, 0)]))
        visited = set()

        while queue:
            row, col, count = queue.popleft()
            if grid[row][col] == 0:
                return count
            if (row, col) in visited:
                continue
                
            visited.add((row, col))

            if row + 1 < self.R and grid[row + 1][col] != -1:
                queue.append((row + 1, col, count + 1))
            if row - 1 >= 0 and grid[row - 1][col] != -1:
                queue.append((row - 1, col, count + 1))
            if col + 1 < self.C and grid[row][col + 1] != -1: 
                queue.append((row, col + 1, count + 1))
            if col - 1 >= 0 and grid[row][col - 1] != -1:
                queue.append((row, col - 1, count + 1))
        
        return 0
        

            






            



        