class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Dictionary method
        // Key, value = value, index
        Dictionary<Integer, Integer> d = new Hashtable<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int current_num = nums[i];
            int complement = target - current_num;

            if (((Hashtable<Integer, Integer>) d).containsKey(complement)) {
                int[] return_this = new int[] { d.get(complement), i };
                return return_this;
            }

            d.put(current_num, i);
        }

        return new int[] { 0, 0 };
    }
}