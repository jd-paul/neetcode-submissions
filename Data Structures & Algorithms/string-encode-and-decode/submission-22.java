class Solution {

    public String encode(List<String> strs) {
        String result = "";

        for (String s : strs) {
            result += s.length() + ":" + s;
        }

        return result;
    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            int colonIndex = str.indexOf(":", i); // Find separator
            int length = Integer.parseInt(str.substring(i, colonIndex)); // Extract length
            i = colonIndex + 1;
            result.add(str.substring(i, i + length));
            i += length;
        }

        return result;
    }
}
