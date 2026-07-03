class Solution:
    def climbStairs(self, n: int) -> int:
        dct = {} # List of `n` with their corresponding score

        def helperFunction(n: int) -> int:
            nonlocal dct
            
            if n in dct:
                return dct[n]
                

            # Hard checks to see if it's valid.
            if n < 0:
                return 0
            elif n == 0:
                return 1
            else:
                val_a = helperFunction(n-1)
                val_b = helperFunction(n-2)

                dct[n] = val_a + val_b
                # if val_a > 0:
                #     dct[n-1] = val_a
                # if val_b > 0:
                #     dct[n] = val_b
                
                return val_a + val_b
        
        return helperFunction(n)