from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        # dfs through 1s to find first island
        # bfs from island1 to island2 

        def dfs(row, col):
            visited = set()
            stack = [(row, col)]

            while stack:
                r, c = stack.pop(-1)

                if (r, c) in visited:
                    continue
                visited.add((r, c))
                if grid[r][c] == 1:
                    grid[r][c] = 2

                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    stack.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    stack.append((r - 1, c))
                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    stack.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    stack.append((r, c - 1))
        
        def bfs(row, col):
            visited = set()
            queue = deque([(row, col, 0)])
            visited.add((row, col))

            # seed the bfs with every valid start point
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        queue.append((r, c, 0))
                        visited.add((r, c))

            while queue:
                r, c, nodesTraveled = queue.popleft()

                visited.add((r, c))

                if grid[r][c] == 2:
                    return nodesTraveled - 1

                if r + 1 < len(grid) and (r + 1, c) not in visited:
                    visited.add((r + 1, c))
                    queue.append((r + 1, c, nodesTraveled + 1))
                if r - 1 >= 0 and (r - 1, c) not in visited:
                    visited.add((r - 1, c))
                    queue.append((r - 1, c, nodesTraveled + 1))
                if c + 1 < len(grid[0]) and (r, c + 1) not in visited:
                    visited.add((r, c + 1))
                    queue.append((r, c + 1, nodesTraveled + 1))
                if c - 1 >= 0 and (r, c - 1) not in visited:
                    visited.add((r, c - 1))
                    queue.append((r, c - 1, nodesTraveled + 1))

        found = False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                if found:
                    break
            if found:
                break
                    

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs(r,c)
        




        


