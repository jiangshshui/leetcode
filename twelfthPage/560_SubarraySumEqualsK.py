# class Solution:
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         dp=[0]
#         for num in nums:
#             dp.append(dp[-1]+num)
#
#         ans=0
#         for i in range(0,len(dp)):
#             for j in range(i+1,len(dp)):
#                 if dp[j]-dp[i]==k:
#                     ans+=1
#
#         return ans

from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m=defaultdict(int)
        m[0]=1
        cnt=0
        s=0
        for num in nums:
            s+=num
            # if s-k in m:
            cnt+=m[s-k]
            m[s] += 1
        return cnt



if  __name__=="__main__":
    s=Solution()
    print(s.subarraySum([1,1,1], k = 2))
    print(s.subarraySum([1],0))