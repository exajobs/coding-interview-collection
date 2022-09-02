class Solution {
    public int findNthDigit(int n) {
		int len = 1;
		long count = 9;
		int start = 1;
        // https://leetcode.com/problems/nth-digit/discuss/88363/Java-solution
		while (n > len * count) {
			n -= len * count;
			len += 1;
			count *= 10;
			start *= 10;
		}
		start += (n - 1) / len;
		String s = Integer.toString(start);
		return Character.getNumericValue(s.charAt((n - 1) % len));
    }
}
