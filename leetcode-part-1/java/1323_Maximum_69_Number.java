class Solution {
    public int maximum69Number (int num) {
        // Replace first 6 with 9 if exists
        return Integer.valueOf(String.valueOf(num).replaceFirst("6", "9"));
    }

    /*
    public int maximum69Number (int num) {
        char[] chars = Integer.toString(num).toCharArray();
        // Replace first 6 with 9 if exists
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '6') {
                chars[i] = '9';
                break;
            }
        }
        return Integer.parseInt(new String(chars));
    }*/
}
