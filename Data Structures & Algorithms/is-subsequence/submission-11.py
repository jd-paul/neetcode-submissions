class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        n = len(t)

        while r < n and l < len(s):
            if s[l] == t[r]:
                l+=1
            r+=1

        return l == len(s)