class Solution:
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.memo = {}
        self.alphabet = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            26: "Z"
        }

        return self.dfs(0)


    """
    1012

    10 is always 10

    1 can become 12 or just 1
    """
    def dfs(self, index: int) -> int:
        # Case 1A: Finished up
        if index == len(self.s):
            return 1
        
        # Case 1B: We are zero.
        if self.s[index] == "0":
            return 0
        
        """
        Case 2: Not yet finished, so we determine how many variations of words we can do.
        Case 2A: Our current ch is `1` or `2` and the next ch is `0`
        Case 2B: Our current ch is `1` and the next ch is `123456789`
            Either keep current ch OR we do `1` + `second ch`
        Case 2C: Our current ch is `2` and the next ch is `123456`
            Either keep current ch OR we do `2` + `second ch`
        """

        if index in self.memo:
            return self.memo[index]

        if index+1 < len(self.s):
            l, r = self.s[index], self.s[index+1]

            if l == "1" and r == "0" or l == "2" and r == "0":
                result = self.dfs(index+2)
                self.memo[index] = result
                return result
            
            elif l == "1" and r in "123456789":
                a, b = None, None
                a = self.dfs(index+1)
                b = self.dfs(index+2)
                result = a + b
                self.memo[index] = result
                return result

            elif l == "2" and r in "123456":
                a, b = None, None
                a = self.dfs(index+1)
                b = self.dfs(index+2)
                result = a + b
                self.memo[index] = result
                return result
            
            else:
                result = self.dfs(index+1)
                self.memo[index] = result
                return result
        else:
            result = self.dfs(index+1)
            self.memo[index] = result
            return result

        

        self.memo[index] = result
        return result