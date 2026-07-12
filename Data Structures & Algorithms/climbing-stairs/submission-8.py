class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        # Key, value = current, value

        # Create a self helper function.
        def helperFunction(current):            
            if current == 0:
                return 1
            elif current < 0:
                return 0
            
            # Check if in cache. If not, memoize.
            elif current in cache:
                return cache[current]
            elif not current in cache:
                cache[current-1] = helperFunction(current-1)
                cache[current-2] = helperFunction(current-2)
                return cache[current-1] + cache[current-2]
            
            else:
                return helperFunction(current-1) + helperFunction(current-2)
        
        return helperFunction(n)