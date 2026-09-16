class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[0] < nums[-1]:
            return nums[0]

        while l <= r: 
            m = (l + r) // 2

            if nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
