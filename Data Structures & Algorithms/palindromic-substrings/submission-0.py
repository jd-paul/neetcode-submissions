class Solution:

    """
    Strategy is to expand outwardly.
    If it is a valid palindrome, we keep appending.
    """
    def countSubstrings(self, s: str) -> int:
        paliCount = 0

        for i in range(0, len(s)):

            # Iterate through odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                paliCount += 1
                l -= 1
                r += 1
            
            # Iterate through even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                paliCount += 1
                l -= 1
                r += 1
        
        return paliCount