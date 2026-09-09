class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        visited = set()

        R = len(grid)
        C = len(grid[0])

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 0:
                    continue
                if (row, col) in visited:
                    continue
                
                queue = deque([(row, col)])

                area = 0

                while queue:
                    r, c = queue.popleft()

                    if (r, c) in visited:
                        continue
                    
                    visited.add((r,c))
                    area += 1

                    if r + 1 < R and grid[r + 1][c] == 1:
                        queue.append((r + 1, c))
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        queue.append((r - 1, c))
                    if c + 1 < C and grid[r][c + 1] == 1:
                        queue.append((r, c + 1))
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        queue.append((r, c - 1))
    
                maxArea = max(area, maxArea)

        return maxArea












        