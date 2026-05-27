class Solution {
    /*
    First Pass (Left to Right - Prefix Product)
        Traverse nums, storing prefix products in output[i], excluding nums[i].
        output[i] = product of all elements before i.

    Second Pass (Right to Left - Suffix Product)
        Traverse nums from right to left.
        Keep track of the suffix product and multiply it with output[i].
        output[i] *= product of all elements after i.
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
