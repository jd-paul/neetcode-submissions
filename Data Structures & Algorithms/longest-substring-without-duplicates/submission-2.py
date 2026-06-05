class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0

        char_set = set() # Container for unique strings

        while end < len(s):
            
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            
            char_set.add(s[end])

            max_len = max(max_len, end - start + 1)

            end += 1
        return max_len