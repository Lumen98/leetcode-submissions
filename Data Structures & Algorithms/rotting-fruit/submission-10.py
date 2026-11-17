class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        R = len(grid)
        C = len(grid[0])

        fresh = 0

        rotten = collections.deque()
        visited = set()
        minutes = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        if len(rotten) == 0:
            if fresh == 0:
                return 0
            return -1

        if fresh == 0:
            return 0


        while fresh > 0:

            numRotten = len(rotten)

            for i in range(numRotten):
                r, c = rotten.popleft()

                if (r, c) in visited:
                    continue
                if grid[r][c] == 0:
                    visited.add(r, c)
                    continue
                
                if r + 1 < R and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    rotten.append((r + 1, c))
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    rotten.append((r - 1, c))
                if c + 1 < C and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    rotten.append((r, c + 1))
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    rotten.append((r, c - 1))
            
            minutes += 1
            if fresh == 0:
                return minutes
            if not rotten:
                return -1
        
        return minutes








