class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        # count = {1 : 3, 2 : 2, 3 : 1}

        maxHeap = [[-cnt, n] for n, cnt in count.items()]
        heapq.heapify(maxHeap)
        # filled in with -count and number pairs -> [-cnt, n]
        res = []

        for i in range(k):
            pair = heapq.heappop(maxHeap) 
            res.append(pair[1])
            if len(res) == k:
                return res





