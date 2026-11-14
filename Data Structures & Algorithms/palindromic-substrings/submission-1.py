class Solution:
    """
    Strategy is to expand outwardly.
    If it is a valid palindrome, we keep appending.
    """
    def countSubstrings(self, s: str) -> int:
        self.paliCount = 0

        def helper(l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.paliCount += 1
                l -= 1
                r += 1


        for i in range(0, len(s)):
            l, r = i, i

            helper(l, r)
            helper(l, r+1)
        
        return self.paliCount
    
        