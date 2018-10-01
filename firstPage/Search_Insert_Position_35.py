class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index in range(len(nums)):
            if target<=nums[index]:
                return index
        return index+1