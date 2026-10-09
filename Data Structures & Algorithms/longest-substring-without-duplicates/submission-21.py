class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        l, r = 0, 1 # Sliding window
        n = len(s)
        max_window_size = 0

        # Initial checks for short strings
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            return 2

        # Initialising for sliding window
        if s[l] == s[r]:
            dct[s[l]] = 2
        else:
            dct[s[l]] = 1

        # Version that does NOT utilise uniqueDict
        while r < n:
            if s[r] in dct:
                dct[s[r]] += 1
            else:
                dct[s[r]] = 1
            
            while dct[s[r]] > 1 and l < r:
                # Do a while loop cleaning out the window so
                # that there are no more loops

                dct[s[l]] -= 1
                l += 1
            
            max_window_size = max(max_window_size, r - l + 1)
            r += 1
        
        return max_window_size