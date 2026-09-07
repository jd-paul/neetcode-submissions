class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dct = {}

        # iterate once
        for char in magazine:
            if char in dct:
                dct[char] += 1
            else:
                dct[char] = 1
        
        # iterate ransomNote
        for char in ransomNote:
            if char in dct:
                if dct[char] <= 0:
                    return False
                dct[char] -= 1
                    
            else:
                return False
        

        return True