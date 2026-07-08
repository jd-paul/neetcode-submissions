class Solution:
    def trap(self, height: List[int]) -> int:
        # Determine the max height.
        """
        We can store the prefix maximum in an array by
        iterating from left to right and the suffix maximum
        in another array by iterating from right to left. For
        example, in [1, 5, 2, 3, 4], for the element 3, the prefix
        maximum is 5, and the suffix maximum is 4. Once these arrays
        are built, we can iterate through the array with index i and
        calculate the total water trapped at each position using the
        formula: min(prefix[i], suffix[i]) - height[i]. 
        """

        """
        height = [0,2,0,3,1,0,1,3,2,1]

        We calculate for a concept called 'prefix max' and 'suffix' max.
        Basically, at an index, we determine the maximum height

        height = [1, 5, 2, 3, 4]

        prefix_max = [1, 5, 5, 5, 5]
        suffix_max = [5, 5, 4, 4, 4]

        max_water = min(prefix_max[i], suffix_max[i] - height[i])

        return max(max_water)
        """

        # Determine prefix
        prefix = [None] * len(height)
        tmp_max = 0
        for i in range(0, len(height)):
            tmp_max = max(height[i], tmp_max)
            prefix[i] = tmp_max
        
        # Determine suffix
        suffix = [None] * len(height)
        tmp_max = 0
        for i in range(len(height)-1, -1, -1):
            tmp_max = max(height[i], tmp_max)
            suffix[i] = tmp_max
        
        # Determine
        total_water = 0
        for i in range(len(height)):
            total_water += min(prefix[i], suffix[i]) - height[i]
        
        return total_water