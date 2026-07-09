class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
            if freq[nums[i]] > 1:
                return True
        return False

        