# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                return [seen[n], i]
            else:
                diff = target - n
                seen[diff] = i

        raise Exception("assumed to have valid answer")
