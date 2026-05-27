class Solution {
    public boolean isPalindrome(String s) {
        // Step 1: Convert to lowercase and remove non-alphanumeric characters
        String cleaned = "";
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleaned += Character.toLowerCase(c);
            }
        }

        // Step 2: Check if the cleaned string is a palindrome
        int left = 0, right = cleaned.length() - 1;
        while (left < right) {
            if (cleaned.charAt(left) != cleaned.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
