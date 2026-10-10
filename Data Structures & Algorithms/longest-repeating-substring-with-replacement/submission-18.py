class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "XYYXX", k = 1
        """

        l, r = 0, 1
        max_size = 1
        current_size = 0
        k_used = 0
        n = len(s)
        dct = {}

        # Initialise
        dct[s[l]] = 1

        while l < n and r < n:
            # Iterate and add the rightmost value now
            if s[r] in dct:
                dct[s[r]] += 1
            else:
                dct[s[r]] = 1

            # Check if we've reached past our limit
            current_size = r - l + 1
            k_used = current_size - max(dct.values())
            
            while k_used > k:
                dct[s[l]] -= 1
                l+=1
                current_size = r - l
                k_used = current_size - max(dct.values())
            
            r+=1
            max_size = max(max_size, current_size)
        
        return max_size