class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        self.digits = digits
        self.res = []
        self.dct = {}
        self.digits = digits
        self.phone_number = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.recurse(0, "")
        return self.res


    def recurse(self, i: int, s: str):
        # Base case: We reached the end
        if i >= len(self.digits):
            self.dct[s] = 1
            self.res.append(s)
            return
        
        # Two cases.
        # Add current string and move on
        current_iteration = self.phone_number[self.digits[i]] # 2: "abc"
        for idx in range(0, len(current_iteration)):
            s_copy = s + current_iteration[idx]
            self.recurse(i+1, s_copy)