class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1)
        
        dct_s1, dct_s2 = {}, {} # Initialising step
        alphabet = "qwertyuiopasdfghjklzxcvbnm"

        for ch in alphabet:
            dct_s1[ch], dct_s2[ch] = 0, 0
        
        for i in range(0, r):
            dct_s1[s1[i]] += 1
            dct_s2[s2[i]] += 1

        while r < len(s2):
            if dct_s1 == dct_s2:
                return True
            
            left_ch = s2[l]
            right_ch = s2[r]
            
            dct_s2[left_ch] -= 1
            dct_s2[right_ch] += 1

            l+=1
            r+=1
        
        if dct_s1 == dct_s2:
            return True

        return False