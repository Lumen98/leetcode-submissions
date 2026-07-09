from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        res = []

        for i in range(len(nums)):
            freq[nums[i]] += 1

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        for i in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)

        return res

