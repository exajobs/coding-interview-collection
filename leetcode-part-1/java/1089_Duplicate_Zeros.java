class Solution {
    public void duplicateZeros(int[] arr) {
        int movePos = 0;
        int lastPos = arr.length - 1;
        // Only check [0, lastPos - movePos]
        for (int i = 0; i <= lastPos - movePos; i++) {
            if (arr[i] == 0) {
                // Special case
                if (i == lastPos - movePos) {
                    arr[lastPos] = 0;
                    lastPos--;
                    break;
                }
                movePos++;
            }
        }
        lastPos = lastPos - movePos;
        for (int i = lastPos; i >= 0; i--) {
            if (arr[i] == 0) {
                arr[i + movePos] = 0;
                movePos--;
                arr[i + movePos] = 0;
            } else {
                arr[i + movePos] = arr[i];
            }
        }
    }
}
