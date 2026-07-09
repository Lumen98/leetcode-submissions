from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        R = len(grid)
        C = len(grid[0])
        fresh = 0
        res = 0
        
        queue = deque([])
        visited = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        if fresh == 0:
            return 0
        
        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
                if fresh == 0:
                    return res + 1
            
                # go through all 4 positions from each (r,c) --> rottenize the fruit
                # whenever we rottenize a fruit, add that to queue2

                if r + 1 < R and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    queue.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    queue.append((r - 1, c))
                if c + 1 < C and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    queue.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    queue.append((r, c - 1))
            
            res += 1
        
        if fresh == 0:
            return res
        return -1










