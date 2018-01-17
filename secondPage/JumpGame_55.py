'''
第一种解法
'''
# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         length=len(nums)
#         index=0
#         premaxposition=0
#         maxposition = nums[index] + index
#         innermaxposition=maxposition
#         while maxposition<length-1:
#             for i in range(premaxposition+1,maxposition):
#                 innermaxposition=max(innermaxposition,nums[i]+i)
#             if innermaxposition>=length-1:
#                 return True
#             if innermaxposition==maxposition:
#                 if nums[maxposition]==0:
#                     return False
#                 else:
#                     premaxposition=maxposition
#                     innermaxposition =maxposition=nums[maxposition]+maxposition
#             else:
#                 premaxposition=maxposition
#                 maxposition=innermaxposition
#         return True


class Solution(object):
    def canJump(self, nums):
        last=len(nums)-1
        position=len(nums)-2
        while position>=0:
            if nums[position]+position>=last:
                last=position
            position-=1
        if last==0:
            return True
        else:
            return False



s=Solution()
print(s.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))
print(s.canJump([1,2,3]))
print(s.canJump([1,1,0,1]))
