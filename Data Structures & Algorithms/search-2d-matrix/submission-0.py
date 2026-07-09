class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        binarySearch = [num for row in matrix for num in row]

        l, r = 0, len(binarySearch) - 1

        while l <= r:
            m = (l + r) // 2

            if binarySearch[m] == target:
                return True
            elif binarySearch[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
