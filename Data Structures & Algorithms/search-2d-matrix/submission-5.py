class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        # extract the first col and binary search that for closest to target that is less than target
        # extract that row then binary search that for closest to target

        col = [row[0] for row in matrix]

        l, r = 0, len(col) - 1

        while l <= r:
            m = (l + r) // 2

            if col[m] < target:
                l = m + 1
            elif col[m] > target:
                r = m - 1
            else:
                return True
        
        row = matrix[r]

        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True

        return False









