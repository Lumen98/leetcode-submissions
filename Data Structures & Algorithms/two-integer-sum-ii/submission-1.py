class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        l = 0

        for r in range(len(numbers)):
            if target - numbers[r] in numbers:
                l = r
                while target - numbers[l] != numbers[r]:
                    r += 1
                return [l + 1, r + 1]
            
