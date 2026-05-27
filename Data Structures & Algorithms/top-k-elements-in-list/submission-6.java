class Solution {
    /*
    Create a hashmap and put frequency of elements.
    Then convert it into a list sorted based on frequency.
    Return top 'k' elements
    */
    
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        int[] result = new int[k];

        for (int n : nums) {
            dict.put(n, dict.getOrDefault(n, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> sortedList = new ArrayList<>(dict.entrySet());
        sortedList.sort((a, b) -> b.getValue() - a.getValue());

        int i = 0;
        for (Map.Entry<Integer, Integer> entry : sortedList) {
            result[i] = entry.getKey();
            i++;
            if (i == k) break;
        }

        return result;
    }
}
