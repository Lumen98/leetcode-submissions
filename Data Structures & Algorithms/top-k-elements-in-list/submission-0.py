class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return []
        hashmap = {}
        solutionArray = [0]*k

        for index, value in enumerate(nums):
            hashmap[value] = hashmap.get(value, 0) + 1
        
        ctr = k
        while ctr > 0:
            maxKey = max(hashmap, key=hashmap.get)
            solutionArray[ctr - 1] = maxKey
            ctr -= 1
            hashmap[maxKey] = -1
        
        return solutionArray

            




            
    

        

        