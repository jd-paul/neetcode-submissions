class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n * 2
        self.dct = {}
        self.output = []

        self.recurse("", 0, 0)
        return self.output
    
    def recurse(self, s: str, b_open: int, b_close: int):
        if b_close > b_open:
            return
        
        if len(s) >= self.n:
            if s not in self.dct and b_open == b_close:
                self.dct[s] = 1
                self.output.append(s)
            return

        """
        Two cases
            1 - Place an open parenthesis `(`
            2 - Place a closed parenthesis `)`
        """
        s_case1 = s
        s_case1 += "("
        s_case2 = s
        s_case2 += ")"

        self.recurse(s_case1, b_open+1, b_close)
        self.recurse(s_case2, b_open, b_close+1)