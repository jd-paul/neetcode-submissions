class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.target = target
        self.seen_values = {}
        self.nums = nums

        self.recurse([], 0, 0)

        return self.output
    
    # Keep a tracker of our total
    def recurse(self, nums, accumulate, start):
        tuple_copy = tuple(sorted(nums))

        if tuple_copy in self.seen_values:
            return

        if accumulate == self.target:
            self.output.append(nums)
            self.seen_values[tuple_copy] = 1
            return
        elif accumulate > self.target:
            self.seen_values[tuple_copy] = 1
            return
        
        for i in range(start, len(self.nums)):
            nums_copy = nums.copy()
            new_num = self.nums[i]

            nums_copy.append(new_num)
            self.recurse(nums_copy, accumulate + new_num, i)