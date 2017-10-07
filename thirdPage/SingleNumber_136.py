class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums=sorted(nums)
        # i=0
        # if len(nums)==1:
        #     return nums[0]
        # while i<len(nums):
        #     if i<len(nums)-1 and nums[i]==nums[i+1] or nums[i]==nums[i-1]:
        #         i+=1
        #         continue
        #     break
        # return nums[i]
        res = 0
        for num in nums:
            res ^= num
        return res

s=Solution()
print(s.singleNumber([12,23,43,54,6,67,12,23,43,54,67]))