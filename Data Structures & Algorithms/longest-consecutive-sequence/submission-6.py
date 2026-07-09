class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 in s:
                continue
            length = 1
            while nums[i] + length in s:
                length += 1
            
            res = max(res, length)
        
        return res



