class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1]*len(nums)
        prefix = 1


        for i in range(len(nums)):
            pref[i] = prefix
            prefix *= nums[i]
    
        postfix = 1

        for i in range(len(nums) - 1,-1,-1):
            pref[i] *= postfix
            postfix *= nums[i]
        
        return pref




