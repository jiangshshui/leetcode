class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        res=0
        low=0
        high=0
        for i in range(len(ages)):
            while low<len(ages) and ages[low]<=ages[i]/2+7:
                low+=1
            if low>i:
                continue
            while high<len(ages) and ages[high]<=ages[i]:
                high+=1
            res+=high-low-1
        return res

# class Solution:
#     def numFriendRequests(self, ages):
#         """
#         :type ages: List[int]
#         :rtype: int
#         """
#         num_in_ages=[0 for _ in range(121)]
#         for age in ages:
#             num_in_ages[age]+=1
#
#         sum_in_ages=[0 for _ in range(121)]
#         for i in range(1,121):
#             sum_in_ages[i]=num_in_ages[i]+sum_in_ages[i-1]
#         res=0
#
#         for i in range(15,121):
#             if num_in_ages[i]!=0:
#                 res+=(sum_in_ages[i]-sum_in_ages[i//2+7]-1)*(num_in_ages[i])
#         return res

s=Solution()
print(s.numFriendRequests([20,20,20]))
print(s.numFriendRequests([16,17,18]))