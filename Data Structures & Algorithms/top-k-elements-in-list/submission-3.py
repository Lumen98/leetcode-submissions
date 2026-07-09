class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        sol = [0]*k

        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        ctr = k
        while ctr > 0:
            maxKey = max(hashmap, key=hashmap.get)
            sol[ctr - 1] = maxKey
            ctr -= 1
            hashmap[maxKey] = -1
        
        return sol
        