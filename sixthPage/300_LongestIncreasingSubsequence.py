'''
n^2的解法
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[1 for _ in range(len(nums))]
        for index,num in enumerate(nums):
            for i in range(index):
                if nums[i]<num:
                    dp[index]=max(dp[index],dp[i]+1)
        return max(dp)
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[1 for _ in range(len(nums))]
        for index,num in enumerate(nums):
            for i in range(index):
                if nums[i]<num:
                    dp[index]=max(dp[index],dp[i]+1)
        return max(dp)
s=Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))