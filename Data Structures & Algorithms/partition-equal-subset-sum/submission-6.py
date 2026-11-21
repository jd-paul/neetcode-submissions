class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        self.nums = nums
        self.total = {}
        self.memo = {}
        t = 0

        for i in nums:
            t += i
        
        if t % 2 != 0:
            return False
        
        return self.recurse(0, t / 2)

    def recurse(self, index: int, value: int):
        if index == len(self.nums):
            return False
        if value == 0:
            return True
        elif value < 0:
            return False

        # Two options.
        a_1 = index + 1
        a_2 = value - self.nums[index]
        b_1 = index + 1
        b_2 = value

        if (a_1, a_2) in self.memo:
            a = self.memo[(a_1, a_2)]
        else:
            a = self.recurse(index+1, value - self.nums[index])
            self.memo[(a_1, a_2)] = a
        
        if a:
            return True
        
        if (b_1, b_2) in self.memo:
            b = self.memo[(b_1, b_2)]
        else:
            b = self.recurse(index+1, value)
            self.memo[(b_1, b_2)] = b
        
        if b:
            
            return True
        return False