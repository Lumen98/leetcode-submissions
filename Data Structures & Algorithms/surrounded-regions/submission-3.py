class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        R = len(board)
        C = len(board[0])

        queue = deque()

        for c in range(C):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[R - 1][c] == "O":
                queue.append((R - 1, c))

        for r in range(R):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][C - 1] == "O":
                queue.append((r, C - 1))
        
        invalid = set(queue)
        visited = set()

        while queue:
            r, c = queue.popleft()

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r + 1 < R and board[r + 1][c] == "O":
                invalid.add((r + 1, c))
                queue.append((r + 1, c))
            if r - 1 >= 0 and board[r - 1][c] == "O":
                invalid.add((r - 1, c))
                queue.append((r - 1, c))
            if c + 1 < C and board[r][c + 1] == "O":
                invalid.add((r, c + 1))
                queue.append((r, c + 1))
            if c - 1 >= 0 and board[r][c - 1] == "O":
                invalid.add((r, c - 1))
                queue.append((r, c - 1))
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    if (r, c) in invalid:
                        continue
                    board[r][c] = "X"
    




            

        
