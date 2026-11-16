class Solution:
    """
    [1, 2, 3, 4, 5] -> As we increase the array, we keep increasing in value provided it's positive.
    [-1, -2, -3, -4] -> 
        -1 =                1
        -1 * -2 =           2
        -1 * -2 * -3 =      -6
        -1 * -2 * -3 * -4 = 24
    
    As we go through the subarrays, we need to keep track of a maximum product subarray AND a minimum.
    """
    """
    minimum_product
    maximum_product

    There are three cases.

    Starting a new subarray.
    Multiplying with the previous maximum_product
    Multiplying with the previous minimum_product.

    max_product is updated to the maximum of these three
    """
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res