class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        - Array of distinct integers nums
        - Target integer target
        
        Your task is to return a list of all unique combinations
        of nums where the chosen numbers sum to target.
        """

        """
        Let's say we have [2, 5, 6], and target = 5

        [2]
        Options: 2, 5, 6

        [2, 2]
        Options: 2, 5, 6

        [2, 2, 2]
        Options: 2, 5, 6. Failed.

        [2, 2]
        Options: 2, 5

        """
        

        correct = []
        
        def dfs(index, current_set):
            if sum(current_set) == target:
                correct.append(current_set)
                return 0
            elif sum(current_set) > target:
                return 0
            else:
                for i in range(index, len(nums)):
                    new_set = current_set[:]
                    new_set.append(nums[i])
                    dfs(i, new_set)
    
        # Method: Keep trying from 'i'
        
        
        dfs(0, [])
        
        
        return correct