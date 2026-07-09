class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, 1
        target2 = 0
        while leftPtr < rightPtr and rightPtr < len(nums):
            target2 = target - nums[leftPtr]
            if target2 in nums:
                if nums[leftPtr] + nums[rightPtr] == target:
                    nums.clear()
                    nums.append(leftPtr)
                    nums.append(rightPtr)
                    return nums
                rightPtr += 1
            else:
                leftPtr += 1
                rightPtr = leftPtr + 1
        nums.clear()
        nums.append(leftPtr + 1)
        nums.append(rightPtr - 1)
        return nums
            

        