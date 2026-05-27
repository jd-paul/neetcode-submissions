class Solution {

    public String encode(List<String> strs) {
        String result = "";
        
        for (String s : strs) {
            result += s.length() + ":" + s; // Store length followed by ':'
        }
        
        return result;
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            int colonIndex = str.indexOf(":", i); // Find separator
            int length = Integer.parseInt(str.substring(i, colonIndex)); // Extract length
            i = colonIndex + 1; // Move past ':'
            result.add(str.substring(i, i + length)); // Extract string
            i += length; // Move to next entry
        }

        return result;
    }
}
