from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        horiz, vert, diag = defaultdict(set), defaultdict(set), defaultdict(set)



        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                curr = int(board[r][c])
                
                if curr in horiz[r] or curr in vert[c] or curr in diag[(r // 3, c // 3)]:
                    return False
                
                horiz[r].add(curr)
                vert[c].add(curr)
                diag[(r // 3, c // 3)].add(curr)

        return True


        