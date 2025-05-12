public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        // Initialize a StringBuilder to hold the encoded strings
        StringBuilder res = new StringBuilder();

        // Iterate over each string in the input list
        for (String s : strs) {
            // Replace each occurrence of '/' with '//'
            // This is our way of "escaping" the slash character
            // Then add our delimiter '/:' to the end
            res = res.append((s.replace("/", "//"))).append("/:");
        }

        // Return the final encoded string
        return res.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        // Initialize a List to hold the decoded strings
        ArrayList<String> decodedStrings = new ArrayList<>();

        // Initialize a StringBuilder to hold the current string being built
        String currentString = "";

        // Initialize an index 'i' to start of the string
        int i = 0;

        // Iterate while 'i' is less than the length of the encoded string
        while (i < s.length()) {
            // If we encounter the delimiter '/:'
            if (i + 1 < s.length() && s.charAt(i) == '/' && s.charAt(i + 1) == ':') {
                // Add the currentString to the list of decodedStrings
                decodedStrings.add(currentString.toString());

                // Clear currentString for the next string
                currentString = "";

                // Move the index 2 steps forward to skip the delimiter
                i += 2;
            }
            // If we encounter an escaped slash '//'
            else if (i + 1 < s.length() && s.charAt(i) == '/' && s.charAt(i + 1) == '/') {
                // Add a single slash to the currentString
                currentString = currentString + ('/');

                // Move the index 2 steps forward to skip the escaped slash
                i += 2;
            }
            // Otherwise, just add the character to currentString and move the index 1 step forward.
            else {
                currentString = currentString + (s.charAt(i));
                i++;
            }
        }

        // Return the list of decoded strings
        return decodedStrings;
    }
}