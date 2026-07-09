from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # k=number, v=freq

        res = []

        
        maxHeap = [[-cnt, num] for num, cnt in freq.items()]

        heapq.heapify(maxHeap)

        for i in range(k):
            cnt, num = heapq.heappop(maxHeap)
            res.append(num)
        

        return res
