class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> dictS = new HashMap<>();
        HashMap<Character, Integer> dictT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            dictS.put(c, dictS.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            dictT.put(c, dictT.getOrDefault(c, 0) + 1);
        }

        return dictS.equals(dictT);
    }
}
