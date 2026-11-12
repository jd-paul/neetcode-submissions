class Solution:
    """
    Loop through all numbers,
    """
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.visited = {}
        self.house_checker = {}
        max_value = 0
        for i in range(len(self.nums)):
            self.visited[i] = False
            self.house_checker[i] = True
        
        for index, value in enumerate(self.nums): # Loop through all
            dct_copy = self.visited.copy()
            max_value = max(self.recurse(index, 0, dct_copy), max_value)

        return max_value

    """ Two cases
    Case 1 - Not yet visited all valid houses so we iterate
    Case 2 - Visited all houses so we return our total
    """
    def recurse(self, house_number: int, total: int, visited: dict) -> int:
        if visited == self.house_checker: # Base case 1: Visited all housees
            return total
        
        # Step 1: Assuming our current node is valid...
        total += self.nums[house_number] # Add to total
        # Make current, left, and right nodes visited.
        visited[house_number] = True

        if not house_number - 1 < 0:
            visited[house_number - 1] = True
        if not house_number + 1 > len(self.nums):
            visited[house_number + 1] = True
        
        # Loop through unvisited houses
        for index, value in enumerate(self.nums):
            if visited[index] == False:
                visited_copy = visited.copy()
                return self.recurse(index, total, visited_copy)
            continue
        
        # No more available houses
        return total