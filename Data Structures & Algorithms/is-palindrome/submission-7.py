class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        ptrStart = 0
        ptrEnd = len(s) - 1

        

        while ptrEnd > ptrStart:
            if not s[ptrEnd] == s[ptrStart]:
                return False
            ptrEnd-=1
            ptrStart+=1
        
        return True