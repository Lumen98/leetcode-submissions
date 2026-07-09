class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()

        res = 0

        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue

                if ((r, c)) in visited:
                    continue

                stack = [(r, c)]
                islandCount = 0

                while stack:
                    row, col = stack.pop(-1)

                    if ((row, col)) in visited:
                        continue
                    visited.add((row, col))
                    islandCount += 1

                    if row + 1 < R and grid[row + 1][col] == 1:
                        stack.append((row + 1, col))
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        stack.append((row - 1, col))
                    if col + 1 < C and grid[row][col + 1] == 1:
                        stack.append((row, col + 1))
                    if col - 1 >= 0  and grid[row][col - 1] == 1:
                        stack.append((row, col - 1))
                
                res = max(res, islandCount)
                

        return res

