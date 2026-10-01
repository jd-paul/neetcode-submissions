class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Logic checks
        if len(s2) < len(s1):
            return False
        
        # Setup code
        dct = {}
        size = len(s1)

        for i in s1:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        
        for i in range(0, size):
            ch = s2[i]
            if ch in dct:
                dct[ch] -= 1
        
        if all(v == 0 for v in dct.values()):
            return True # Initial check

        # Slide loop
        for i in range(size, len(s2)):
            # Restore values
            ch = s2[i - size]
            if ch in dct:
                dct[ch] += 1
            
            # Chip away
            ch = s2[i]
            if ch in dct:
                dct[ch] -= 1

            if all(v == 0 for v in dct.values()):
                return True # Check

        return False