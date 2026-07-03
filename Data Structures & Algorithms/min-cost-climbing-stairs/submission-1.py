class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        index_max = len(cost)-1

        def climbStairs(i: int):

            # Base cases.
            if i == index_max:
                cache[i] = cost[i]
                return cost[i]
            elif i > index_max: # Need to bake safety into the call function itself
                return 0

            else:
                if i in cache:
                    return cache[i]
                else:
                    cache[i] = cost[i] + min(climbStairs(i+1), climbStairs(i+2))
                    return cache[i]
                    

        return min(climbStairs(0), climbStairs(1))