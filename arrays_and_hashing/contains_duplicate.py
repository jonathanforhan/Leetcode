"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()

        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
