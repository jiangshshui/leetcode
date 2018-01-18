#超时
# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<=2:
#             return n
#         return self.climbStairs(n-1)+self.climbStairs(n-2)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        dp=[0 for i in range(n+1)]
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

s=Solution()
print(s.climbStairs(1))