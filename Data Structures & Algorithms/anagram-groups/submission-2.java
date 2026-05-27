class Solution {
    
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


/*
✔ Step 1: Replace the dictHashMap structure with HashMap<String, List<String>>.
✔ Step 2: Sort each string and use it as a key in the HashMap.
✔ Step 3: Use this HashMap to group anagrams together.
✔ Step 4: Extract values from the HashMap and return them.
*/