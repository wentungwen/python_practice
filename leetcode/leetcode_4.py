class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums2 += nums1
        nums2.sort()
        length = len(nums2)
        if length % 2 == 0:
            mid_idx = int(length/2-1)
            mid2_idx = int(mid_idx+1)
            median = (nums2[mid_idx] + nums2[mid2_idx])/2
        else:
            mid_idx = (length-1)/2
            median = nums2[int(mid_idx)]

        formatted_median = "{:.5f}".format(median)
        print(formatted_median)



s = Solution()
s.findMedianSortedArrays([1, 3], [2])
s.findMedianSortedArrays([1, 2], [3, 4])



# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.