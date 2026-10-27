class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl",
                "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res, path = [], []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))   # one join per answer, O(n) — unavoidable
                return
            for c in phone[digits[i]]:
                path.append(c)              # O(1), mutate in place
                backtrack(i + 1)
                path.pop()                  # undo — this is the "backtrack"

        backtrack(0)
        return res