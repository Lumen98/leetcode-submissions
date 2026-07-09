class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        numSet = set()
        maxLength = 0

        for right in range(len(s)):
            while s[right] in numSet:
                numSet.remove(s[left])
                left += 1
            
            if s[right] not in numSet:
                numSet.add(s[right])
            
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength


            

