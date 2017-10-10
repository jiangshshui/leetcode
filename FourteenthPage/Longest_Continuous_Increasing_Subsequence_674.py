class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        max_length=0
        while i<len(nums):
            cur=1
            while i+1<len(nums) and nums[i]<nums[i+1]:
                i+=1
                cur+=1
            if max_length<cur:
                max_length=cur
            i=i+1
        return max_length
s=Solution()
print(s.findLengthOfLCIS([2,2,2,2,2]))


