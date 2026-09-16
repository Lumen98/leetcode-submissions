class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1


        def binarySearch(array):
            l, r = 0, len(array) - 1

            while l <= r:
                m = (l + r) // 2

                if array[m] == target:
                    return m
                elif array[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return -1


        if nums[0] < nums[-1]:
            # run normal binary search
            return binarySearch(nums)
        else:
            # run a binary search to find the split, then split the lists, then run individual binary searches

            splitIndex = 0

            l, r = 0, len(nums) - 1

            while l <= r:
                m = (l + r) // 2 

                if nums[m] == target:
                    return m 
                if nums[m - 1] > nums[m]:
                    splitIndex = m
                    break
                elif nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            res = binarySearch(nums[0:splitIndex])
            if res != -1:
                return res
            
            res = binarySearch(nums[splitIndex:])
           
            if res != -1:
                return res + splitIndex
            return -1 






