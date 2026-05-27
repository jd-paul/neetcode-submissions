class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return False
        
        # Two pointers, from left to right.
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower().strip()
        left, right = 0, len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True