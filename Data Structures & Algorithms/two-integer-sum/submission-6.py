class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}


        for i in range(0,len(nums)):
            lookingFor = target - nums[i]

            if lookingFor in hashmap:
                return [hashmap[lookingFor],i]
            
            hashmap[nums[i]] = i 
        