import java.util.HashMap;

public class MF {
    public static void main(String[] args) {
        // NOTE: The following input values are used for testing your solution.

        // mostFrequent(array1) should return 1.
        int[] array1 = {1, 3, 1, 3, 2, 1};
        // mostFrequent(array2) should return 3.
        int[] array2 = {3, 3, 1, 3, 2, 1};
        // mostFrequent(array3) should return null.
        int[] array3 = {};
        // mostFrequent(array4) should return 0.
        int[] array4 = {0};
        // mostFrequent(array5) should return -1.
        int[] array5 = {0, -1, 10, 10, -1, 10, -1, -1, -1, 1};
    }

    // Implement your solution below.
    public static Integer mostFreqent(int[] givenArray) {
        Integer maxCount = -1; Integer maxItem = null;
        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        for (int i : givenArray) {
            if (count.containsKey(i)) {
                Integer newVal = count.get(i) + 1;
                count.put(i, newVal);
            } else {
                count.put(i, 1);
            }
            if (count.get(i) > maxCount) {
                maxCount = count.get(i);
                maxItem = i;
            }
        }
        return maxItem;
    }
}
