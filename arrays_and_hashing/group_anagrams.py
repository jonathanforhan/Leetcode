# https://leetcode.com/problems/group-anagrams/


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)

        for s in strs:
            key = defaultdict(int)

            for c in s:
                key[c] += 1

            group[frozenset(key.items())].append(s)

        return list(group.values())
