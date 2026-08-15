public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dct = new Dictionary<int, int>();
        // `var dct = new Dictionary<int, int>();` also works
        // We store the value as the key, and the index as the value

        for (int k = 0; k < nums.Length; k++)
        {
            int current = nums[k];
            int complement = target - current;

            if (dct.ContainsKey(complement))
            {
                // Return this list
                return new int[] {dct[complement], k};
            }
            else
            {
                dct[current] = k; // current value -> index
            }
        }

        return Array.Empty<int>();
    }
}