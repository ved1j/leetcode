class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = len(s) - 1
        res = 0

        for r in range(len(s) - 1, -1, -1):
            while s[r] in charSet:
                charSet.remove(s[l])
                l -= 1
            charSet.add(s[r])
            res = max(res, l - r + 1)
        return res