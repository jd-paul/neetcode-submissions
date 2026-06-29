class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method: iterative expansion
        subsets = [[]]
        
        for i in nums:
            snapshot = subsets[:]

            # Build from current subsets
            for lst in snapshot:
                new_lst = lst[:]
                
                new_lst.append(i)
                if new_lst not in subsets:
                    subsets.append(new_lst)    
        
        return subsets