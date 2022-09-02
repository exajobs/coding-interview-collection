public class Solution {
    /*public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0, count = 0;
        while (i < flowerbed.length) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i++] = 1;
                count++;
            }
             if(count >= n)
                return true;
            i++;
        }
        return false;
    }*/
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0, curr;
        for (int i = 0; i < flowerbed.length; i++) {
            curr = flowerbed[i];
            if (i - 1 >= 0) curr += flowerbed[i - 1];
            if (i + 1 < flowerbed.length) curr += flowerbed[i + 1];
            if (curr == 0) {
                count++;
                flowerbed[i] = 1;
            }
            if (count >= n) return true;
        }
        return false;
    }
}
