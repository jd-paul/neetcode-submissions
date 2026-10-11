class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Initialise dictionaries of size 26 (The alphabet).

        First dictionary is for s1.
        Second dictionary is for sliding window from s2.
            This makes it easier to do `window == dct_s1`.

        """
        if len(s1) > len(s2):
            return False

        # Initialise dictionaries of size 26
        l, r = 0, len(s1)-1
        window = {}
        dct_s1 = {} # We are comparing to here!
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        for ch in alphabet:
            window[ch] = 0
            dct_s1[ch] = 0

        for i in range(l, r+1): # Initialise the first loop
            ch_s1 = s1[i]
            ch_s2 = s2[i]

            dct_s1[ch_s1] += 1
            window[ch_s2] += 1

        while l < len(s2) and r < len(s2)-1:
            if window == dct_s1:
                return True
            
            # Move forward
            l_ch = s2[l]
            r_ch = s2[r+1]

            window[l_ch] -= 1
            window[r_ch] += 1
            
            l+=1
            r+=1
        
        if window == dct_s1:
            return True
            
        return False




