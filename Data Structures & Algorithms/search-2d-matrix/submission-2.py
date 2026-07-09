class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        matrix = [num for row in matrix for num in row]

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m] == target:
                return True
            elif matrix[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
