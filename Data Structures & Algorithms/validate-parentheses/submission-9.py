class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        opening = "({["
        closing = "]})"

        dct = {
            "(": ")",
            "{": "}",
            "[": "]"
        }        

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if len(stack) <= 0:
                    return False

                elif not i == dct[stack.pop()]:
                    return False
        
        if len(stack) != 0:
            return False
        return True