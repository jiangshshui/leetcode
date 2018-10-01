# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums)<=2:
#             return -1
#         sums=[0]*len(nums)
#         for i in range(1,len(nums)):
#             sums[i]=sums[i-1]+nums[i-1]
#
#         total=sums[-1]+nums[-1]
#         for i in range(len(nums)-1):
#             if sums[i]==(total-nums[i])/2:
#                 return i
#         return -1


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,sum(nums)
        for i in range(len(nums)):
            r-=nums[i]
            if l==r:
                return i
            l+=nums[i]
        return -1

s=Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([-1,-1,-1,-1,-1,-1]))