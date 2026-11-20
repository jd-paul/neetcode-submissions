from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        left = '({['
        dct = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        q = deque()

        for i in s:
            if i in left:
                q.append(i)
            
            else: # Right side parenthesis
                if len(q) == 0:
                    return False
                else:
                    l = q.pop()
                r = dct[i]

                if l != r:
                    return False
        
        return len(q) == 0
