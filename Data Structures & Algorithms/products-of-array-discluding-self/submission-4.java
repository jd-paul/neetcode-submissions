class Solution {
    /*
    Basically it becomes O(n) * 2

    Multiply from left to right, getting only the numbers before it and creating an accumulative
    number from multiplying

    Then do the same from right to left. Two passes are needed.

    */
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];

        // First pass
        output[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            output[i] = output[i - 1] * nums[i - 1];
        }

        // Second pass
        int suffix = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            output[i] *= suffix;
            suffix *= nums[i];
        }

        return output;

    }
}  
