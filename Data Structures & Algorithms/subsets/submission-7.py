class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.seen_values = set()
        self.recurse(nums)
        return self.output
    
    def recurse(self, nums: List[int]):
        self.output.append(nums)
        self.seen_values.add(frozenset(nums))
        
        # Iterate through your options
        n = len(nums)
        for i in range(0, n):
            numsCopy = nums.copy()
            numsCopy.remove(nums[i])

            if frozenset(numsCopy) not in self.seen_values:
                # Here, we place a guard to see if we already iterated on this one before.
                self.recurse(numsCopy)