class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dct = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for ch in s:
            if ch in dct:
                opposite_ch = dct[ch]
                if len(stack) == 0:
                    return False
                prev_ch = stack.pop()
                if opposite_ch != prev_ch:
                    return False
            else:
                stack.append(ch)
                
        
        return len(stack) == 0