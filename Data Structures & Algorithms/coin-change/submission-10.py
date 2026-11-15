class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.ARBITRARY_MAX = 1000000000000
        self.coins = coins
        self.amount = amount
        self.memo = {}

        res = self.recurse(0)
        if res >= self.ARBITRARY_MAX:
            return -1
        return res

    """
    At each step, we have all the options in the coins.
    """
    def recurse(self, total):        
        if total > self.amount:
            return self.ARBITRARY_MAX
        if total == self.amount:
            return 0

        lst = []
        for i in self.coins:
            if total+i in self.memo:
                lst.append(self.memo[total+i])
            else:
                a = 1 + self.recurse(total+i)
                lst.append(a)
                self.memo[total+i] = a
        
        return min(lst)
