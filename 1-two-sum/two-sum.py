class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lastMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lastMap:
                return [lastMap[diff], i]
            lastMap[n] = i
        return