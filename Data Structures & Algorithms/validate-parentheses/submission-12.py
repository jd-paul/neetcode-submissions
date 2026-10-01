class Solution:
    def isValid(self, s: str) -> bool:
        l = "({["

        r = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for ch in s:
            if ch in r:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()

                if r[ch] != bracket:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0