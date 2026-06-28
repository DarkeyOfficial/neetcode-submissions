class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                diffIndex = nums[i+1:].index(diff) + (i + 1)
                return [i, diffIndex]
        return False

# 1 2 3 4 5
# 7 (1, 4)