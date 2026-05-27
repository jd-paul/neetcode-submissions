class Solution {
    /*
    Step 1: Sort each string and use as key. This way, that becomes its unique anagram key
    Step 2: Add the word to a hashmap, adding +1 for each occurrence of the same anagram.
    Step 3: Return
    */

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> returnThis = new ArrayList<>();
        
        HashMap<String, List<String>> dictHashMap = new HashMap<>();

        // Sort each string and use it as a key.
        for (String word : strs) {
            // Sort the characters in the word to get the anagram key
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedKey = new String(charArray);

            // Add the word to the corresponding list in the hashmap
            dictHashMap.putIfAbsent(sortedKey, new ArrayList<>());
            dictHashMap.get(sortedKey).add(word);
        }

        return new ArrayList<>(dictHashMap.values());
    }
    
    // Returns a frequency map
    public HashMap<Character, Integer> getFrequencyMap(String s) {
        HashMap<Character, Integer> dictS = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            dictS.put(c, dictS.getOrDefault(c, 0) + 1);
        }

        return dictS;
    }
}