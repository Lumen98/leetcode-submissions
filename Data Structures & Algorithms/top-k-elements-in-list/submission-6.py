class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {} # count, number 
        freq = [[] for i in range(len(nums) + 1)]
        # index is how many times number occurrs

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)
        
        sol = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                sol.append(n)
                if len(sol) == k:
                    return sol




        