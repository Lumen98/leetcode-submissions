from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])        

        queue = deque() # contains coordinate tuples 
        visited = set()
        fresh = 0 
        minutes = 0

        for r in range(R):
            for c in range(C): 
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return minutes
            

        while fresh > 0:
            numRotten = len(queue)
            for i in range(numRotten):
                r, c = queue.popleft() 

                if (r, c) in visited:
                    continue
                if grid[r][c] == 0:
                    visited.add(r, c)
                    continue
                
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
            
            minutes += 1
            if fresh == 0:
                return minutes
            if not queue:
                return -1 


        return minutes





        

        
