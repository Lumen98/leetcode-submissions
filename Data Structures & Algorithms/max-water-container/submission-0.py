class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        maxWater = 0

        # start on both ends, increment pointer that has the lower value


        while l < r:
            heightMin = min(heights[l], heights[r])

            width = r - l

            maxWater = max(maxWater, (heightMin * width))

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return maxWater
        