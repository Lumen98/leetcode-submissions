class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        R = len(matrix)
        C = len(matrix[0])

        for row in matrix:
            window = range(row[0], row[C - 1] + 1)
            
            if target in window:
                l, r = 0, C - 1
                while l <= r:
                    m = (l + r) // 2

                    if row[m] == target:
                        return True
                    elif row[m] < target:
                        l = m + 1
                    else:
                        r = m - 1

        return False


        
