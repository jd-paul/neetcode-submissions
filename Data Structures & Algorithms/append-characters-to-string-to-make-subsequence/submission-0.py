class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Subsequence has to appear in order.

        s = "coaching"
        t = "coding"
        """

        ptrS, ptrT = 0, 0
        s_len = len(s)
        t_len = len(t)

        while ptrS < s_len and ptrT < t_len:
            s_letter = s[ptrS]
            t_letter = t[ptrT]
        
            if s_letter == t_letter:
                ptrS += 1
                ptrT += 1
            else:
                ptrS += 1
            
            if ptrT == t_len:
                return 0
        
        return t_len - ptrT