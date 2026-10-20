class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.output = []
        options = [True] * len(nums) # True, meaning usable

        self.recurse([], options, 0)

        return self.output
    
    """
    `returned_list` - The list we build up
    `options` - The options we can select from
    `options_total` - The total 'False' in options
    """
    def recurse(self,
        returned_list: list[int],
        options: list[int],
        options_total: list[int]) -> None:
        
        if options_total == len(options):
            if returned_list not in self.output:
                self.output.append(returned_list)
            
            return

        # Iterate through all available options and self.recurse on them.
        for i in range(0, len(options)):
            if options[i]:
                current_value = self.nums[i]

                copy_returned_list = returned_list.copy()
                copy_options = options.copy()

                copy_returned_list.append(current_value)
                copy_options[i] = False

                self.recurse(copy_returned_list, copy_options, options_total + 1)


