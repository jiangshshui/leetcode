class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)
        if total&1==1:
            return False
        target=total//2
        dp=[False for i in range(target+1)]
        dp[0]=True
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[-1]

s=Solution()
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 2, 3, 5]))