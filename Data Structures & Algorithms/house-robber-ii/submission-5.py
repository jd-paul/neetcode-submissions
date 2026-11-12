class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.memo_1 = {}
        self.memo_2 = {}
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 0:
            return 0

        return max(
            self.recurse(1, self.nums, True),
            self.recurse(0, self.nums[0:len(self.nums)-1], False)
        )
    
    def recurse(self, i, nums, which_one):
        if i >= len(nums):
            return 0

        if which_one:
            if i in self.memo_1:
                return self.memo_1[i]
            
            # Two cases: Either skip or add this number
            self.memo_1[i] = max(
                self.recurse(i+1, nums, True), # Skip current
                nums[i] + self.recurse(i+2, nums, True) # Take current and skip to the next
            )
            return self.memo_1[i]

        else:
            if i in self.memo_2:
                return self.memo_2[i]
            
            # Two cases: Either skip or add this number
            self.memo_2[i] = max(
                self.recurse(i+1, nums, False), # Skip current
                nums[i] + self.recurse(i+2, nums, False) # Take current and skip to the next
            )
            return self.memo_2[i]