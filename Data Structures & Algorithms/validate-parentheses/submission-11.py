class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        l = "({["
        r = ")}]"
        dct = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # Keep popping. Good string s = "([{}])"
        for index, value in enumerate(s):
            if value in dct:
                opposite_value = dct[value]
                if len(stack) == 0:
                    return False
                else:
                    current_value = stack.pop()
                if not opposite_value == current_value:
                    return False
            else:
                stack.append(value)
            
        return len(stack) == 0