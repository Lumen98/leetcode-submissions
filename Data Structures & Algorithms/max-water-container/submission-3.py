class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        
        res = 0

        while l < r:
            curr = 0
            if heights[l] < heights[r]:
                curr = heights[l] * (r - l)
                l += 1
            else:
                curr = heights[r] * (r - l)
                r -= 1
            
            res = max(res, curr)
        
        return res




