class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1
        

        for count in hashmap.values():

            if count > 1:
                return True
        
        return False
         