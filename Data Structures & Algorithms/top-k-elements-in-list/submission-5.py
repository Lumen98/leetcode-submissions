class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {number,count}
        freq = [[] for i in range(len(nums) + 1)]
        # index represents count, and number is added to list
        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        sol = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                sol.append(n)
                if len(sol) == k:
                    return sol

            



