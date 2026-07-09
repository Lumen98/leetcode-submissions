from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                squareR = r // 3
                squareC = c // 3
                if int(board[r][c]) in rows[r]:
                    return False
                if int(board[r][c]) in cols[c]:
                    return False
                if int(board[r][c]) in squares[(squareR, squareC)]:
                    return False

                rows[r].add(int(board[r][c]))
                cols[c].add(int(board[r][c]))
                squares[(squareR, squareC)].add(int(board[r][c]))
    

        return True