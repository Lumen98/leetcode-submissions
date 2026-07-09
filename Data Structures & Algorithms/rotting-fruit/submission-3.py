from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # first loop through and find all rotten oranges
        # perform a bfs from the rotten oranges
        # progressivly update rotten oranges

        R = len(grid)
        C = len(grid[0])

        fresh = 0
        res = 0
        
        queue = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        if fresh == 0:
            return 0

        if not queue:
            return -1
        
        curLength = len(queue)

        while queue:
            if fresh == 0:
                res += 1
                return res
            if curLength == 0:
                curLength = len(queue) 
                res += 1
            row, col = queue.popleft()

            if row + 1 < R and grid[row + 1][col] == 1:
                fresh -= 1
                grid[row + 1][col] = 2
                queue.append((row + 1, col))
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                fresh -= 1
                grid[row - 1][col] = 2
                queue.append((row - 1, col))
            if col + 1 < C and grid[row][col + 1] == 1:
                fresh -= 1
                grid[row][col + 1] = 2
                queue.append((row, col + 1))
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                fresh -= 1
                grid[row][col - 1] = 2
                queue.append((row, col - 1))
            
            curLength -= 1

        if fresh != 0:
            return -1

        return res

