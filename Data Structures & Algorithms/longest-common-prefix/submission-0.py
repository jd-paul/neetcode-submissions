class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Iterate from the very end

        bat, bag, band, bank

        """
        max_n = len(min(strs))
        string_builder = ""

        for char_index in range(0, max_n):
            string_builder += strs[0][char_index]
            for word in strs:
                if not (word[char_index] == string_builder[-1]):
                    return string_builder[0:-1]
        
        return string_builder