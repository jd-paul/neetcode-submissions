class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = []

        word = ""
        for character in s:
            if character == " ":
                if word != "":
                    lst.append(word)
                    word = ""
            else:
                word+=character
        
        if word != "":
            return len(word)
        
        return len(lst.pop())