"""
s="abaaabaa"
output=
[["a","b","a","a","a","b","a","a"],["a","b","a","a","a","b","aa"],["a","b","a","a","aba","a"],["a","b","a","aa","b","a","a"],["a","b","a","aa","b","aa"],["a","b","a","aabaa"],["a","b","aa","a","b","a","a"],["a","b","aa","a","b","aa"],["a","b","aa","aba","a"],["a","b","aaa","b","a","a"],["a","b","aaa","b","aa"],["a","baaab","a","a"],["a","baaab","aa"],["aba","a","a","b","a","a"],["aba","a","a","b","aa"],["aba","a","aba","a"],["aba","aa","b","a","a"],["aba","aa","b","aa"],["aba","aabaa"],["abaaaba","a"]]
"""

"""
At each index we have two decisions: we can either partition and start a new string,
or continue without partitioning.

Can you think of an algorithm to recursively traverse all combinations?
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def recurse(i: int):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    recurse(j+1)

                    part.pop()
        
        recurse(0)
        return res

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True