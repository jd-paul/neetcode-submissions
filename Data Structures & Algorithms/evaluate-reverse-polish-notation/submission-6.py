class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok in "+-/*":
                right = stack.pop()
                left = stack.pop()
                stack.append(self.operand(left, right, tok))
            else:
                stack.append(int(tok))
        
        return stack[0]
                    
    # This should calculate for you
    def operand(self, num1: int, num2: int, operation: str) -> int:
        if operation == "*":
            return num1 * num2
        elif operation == "-":
            return num1 - num2
        elif operation == "+":
            return num1 + num2
        elif operation == "/":
            return int(num1 / num2)