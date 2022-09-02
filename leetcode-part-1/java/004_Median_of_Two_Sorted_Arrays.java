public class Solution {
    // example in leetcode book
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    	int p1 = 0, p2 = 0, pos = 0;
    	int ls1 = nums1.length, ls2 = nums2.length;
    	int[] all_nums = new int[ls1+ls2];
    	double median = 0.0;
    	while (p1 < ls1 && p2 < ls2){
    		if (nums1[p1] <= nums2[p2])
    			all_nums[pos++] = nums1[p1++];
    		else
    			all_nums[pos++] = nums2[p2++];
    	}
    	while (p1 < ls1)
    		all_nums[pos++] = nums1[p1++];
    	while (p2 < ls2)
    		all_nums[pos++] = nums2[p2++];
    	if ((ls1 + ls2) % 2 == 1)
    		median = all_nums[(ls1 + ls2) / 2];
    	else
    		median = (all_nums[(ls1 + ls2) / 2] + all_nums[(ls1 + ls2) / 2 - 1]) / 2.0;
        return median;
    }
}
