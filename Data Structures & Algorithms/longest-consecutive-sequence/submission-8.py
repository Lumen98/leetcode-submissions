class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # loop through the array

        numSet = set(nums)

        res = 0 
        needStart = True
        curr = 0
        l = 0

        while l < len(nums):
            if (nums[l] - 1) not in numSet:
                while (nums[l] + curr) in numSet:
                    curr += 1
            
            res = max(res, curr)
            l += 1
            curr = 0 
        
        return res
            






