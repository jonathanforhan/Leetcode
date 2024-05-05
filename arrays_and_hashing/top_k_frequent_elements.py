# https://leetcode.com/problems/top-k-frequent-elements/


from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        # sort by values
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return [n for n, _ in d][:k]
