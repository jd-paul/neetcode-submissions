"""
You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in increasing order.
    The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

"""

"""
matrix = [
    [1,2,4,8],
    [10,11,12,13],
    [14,20,30,40]
]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # The solution is relatively simple. It is more of a translation problem,
        # applying the original binary search principles we solved earlier but into a
        # different data structure [m][n].

        # For now, we can attempt a solution without using AI. It helps unclog our brain.
        
        left = matrix[0][-1]
        right = matrix[-1][-1]

        # Iterate through the matrix. Determine using the min and max to see if target
        # could be between them.

        # Step 1.
        for row in matrix:
            minimum = row[0]
            maximum = row[-1]

            # It's time to search!
            if minimum <= target <= maximum:
                nums = row

                left, right = 0, len(nums)-1

                while left <= right:
                    middle = left + ((right - left) // 2)
                    middle_num = nums[middle]
                    
                    if nums[middle] == target:
                        return True
                    
                    elif middle_num > target:
                        right = middle - 1

                    else:
                        left = middle + 1
            else:
                continue

        return False