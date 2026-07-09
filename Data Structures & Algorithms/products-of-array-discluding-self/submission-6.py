class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        
        curr = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = curr
            curr *= nums[i]

        print(prefix)

        postfix = [1] * len(nums)
        curr = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = curr
            curr *= nums[i]
        
        print(postfix)
        
        nums[0] = postfix[0]
        for i in range(1, len(nums)):
            nums[i] = prefix[i] * postfix[i]

        return nums



        


        


