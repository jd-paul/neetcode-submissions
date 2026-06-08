class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # The idea is you iterate through
        # AAABABB
        # 


        left, right = 0, 0
        max_freq = 0
        char_counts = {}
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_counts:
                char_counts[current_char]+=1
            else:
                char_counts[current_char]=1
            
            max_freq = max(max_freq, char_counts[current_char])

            # Do a check now

            window_length = right - left + 1

            if window_length - max_freq > k: # Is invalid
                char_counts[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length