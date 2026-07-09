class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        R = len(board)
        C = len(board[0])


        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and self.isEdge(r, c, R, C):
                    board = self.dfs(r, c, board, R, C)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "T":
                    board[r][c] = "O"

    def dfs(self, r, c, board, R, C):
        stack = [(r, c)]
        visited = set()

        while stack:
            row, col = stack.pop(-1)
            if ((row, col)) in visited:
                continue
            visited.add((row, col))

            board[row][col] = "T"

            if row + 1 < R and board[row + 1][col] == "O":
                stack.append((row + 1, col))
            if row - 1 >= 0 and board[row - 1][col] == "O":
                stack.append((row - 1, col))
            if col + 1 < C and board[row][col + 1] == "O":
                stack.append((row, col + 1))
            if col - 1 >= 0 and board[row][col - 1] == "O":
                stack.append((row, col - 1))
        
        return board

    def isEdge(self, r, c, R, C):
        if r == 0:
            return True
        if r == R - 1:
            return True
        if c == 0:
            return True
        if c == C - 1:
            return True

        return False