# https://leetcode.com/problems/encode-and-decode-strings/
# https://neetcode.io/problems/string-encode-and-decode (free)


class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join([s + chr(0x03) for s in strs])

    def decode(self, s: str) -> list[str]:
        strs = []
        string = ""

        for c in s:
            if c == chr(0x03):
                strs.append(str(string))
                string = ""
            else:
                string += c

        return strs
