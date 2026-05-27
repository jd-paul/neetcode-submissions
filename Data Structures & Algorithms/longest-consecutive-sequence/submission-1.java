class Solution {
    public int longestConsecutive(int[] nums) {
        int result = 0;

        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        for (int num : nums) {
            if (!numSet.contains(num - 1)) { // Start of a sequence
                int currentNumber = num;
                int tempCounter = 1;

                // Count consecutive numbers
                while (numSet.contains(currentNumber + 1)) {
                    currentNumber++;
                    tempCounter++;
                }

                // Update the maximum length found
                result = Math.max(result, tempCounter);
            }
        }
        return result;
    }
}
