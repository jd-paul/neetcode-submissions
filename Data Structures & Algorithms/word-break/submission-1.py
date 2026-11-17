class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.preMap = {}
        self.memo = {}

        for word in wordDict:
            self.preMap[word] = len(word)

        """
        case - NOT YET DONE but CANNOT FIND ANY VALID RESPONSE
        Do return False. See if other iterations work.
        
        case - NOT YET DONE
        Iterate through all values in self.preMap. If it works, self recurse on that string.

        case - index == len(self.s)
        return True

        If the whole loop fails, return False
        """
        if self.dfs(0):
            return True
        return False

    def dfs(self, index):
        if index in self.memo:
            return self.memo[index]

        if index == len(self.s):
            self.memo[index] = True
            return True

        for key, value in self.preMap.items():
            if index+value > len(self.s):
                continue
            
            current_word = self.s[index:index+value]
            if current_word == key:
                if self.dfs(index+value):
                    self.memo[index] = True
                    return True
        
        self.memo[index] = False
        return False