class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        return list(nums1_set&nums2_set)

s=Solution()
print(s.intersection([1,2,3,4],[2,3]))