class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # loop through the array

        visitedSet = set()

        numSet = set(nums)

        res = 0 
        needStart = True
        curr = 0
        l = 0

        while l < len(nums):
            if nums[l] in visitedSet:
                l += 1
                continue
            
            while (nums[l] + curr) in numSet:
                visitedSet.add(nums[l] + curr)
                curr += 1
            
            res = max(res, curr)
            l += 1
            curr = 0 
        
        return res
            






