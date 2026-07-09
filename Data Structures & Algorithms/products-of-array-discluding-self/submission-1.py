class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = [0] * len(nums)
        # prefix = [0] * (len(nums) - 1)
        # postfix = [0] * len(nums)
        # productPre = 1
        # productPost = 1

        # for index in range(0, len(nums) - 1):
        #     productPre *= nums[index]
        #     prefix[index] = productPre
        
        # for i in prefix:
        #     print(str(i))

        # for i in range(len(nums) - 1, -1, -1):
        #     productPost *= nums[i]
        #     postfix[i] = productPost 
        # postfix.reverse()
        # output[0] = postfix[len(postfix) - 1]
        # output[len(output) - 1] = prefix[len(prefix) - 1]
        # ctr = len(postfix) - 1
        # for i in range(1, len(nums) - 1):
        #     output[i] = prefix[i - 1] * postfix[ctr - 2]
        #     ctr -= 1
        # return output
        # # prefix = [1,2,8]  
        # # postfix = [6,24,48] 
        # # output = [48, 0, 0, 8]

        answer = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        
        answer[0] = postfix[0]
        for i in range(1, len(nums)-1):
            answer[i] = prefix[i] * postfix[i]
        answer[len(answer) - 1] = prefix[len(prefix) - 1]

        print(prefix)
        print(postfix)

        return answer





        
        