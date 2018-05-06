# class Solution:
#     def jump(self,stones,position,step):
#         if position+step==stones[-1] or position+step+1==stones[-1] or position+step-1==stones[-1]:
#             return True
#         if position+step in stones:
#             if self.jump(stones,position+step,step):
#                 return True
#         if step-1>0 and position+step-1 in stones:
#             if self.jump(stones,position+step-1,step-1):
#                 return True
#         if position+step+1 in stones:
#             if self.jump(stones,position+step+1,step+1):
#                 return True
#         return False
#
#
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
#         if len(stones)==1:
#             return True
#         if stones[1]>1:
#             return False
#         if len(stones)==2:
#             return True
#         for i in range(3,len(stones)):
#             if stones[i]>2*stones[i-1]:
#                 return False
#         return self.jump(stones,1,1)


class Solution:
    def helper(self,stones,curstep,pos,memo):
        if pos==len(stones)-1:
            return True
        if (pos,curstep) in memo:
            return memo[(pos,curstep)]
        fin=False
        for step in range(curstep-1,curstep+2):
            idx=self.binarySearch(step+stones[pos],stones[pos+1:])
            if idx!=-1:
                fin=fin or self.helper(stones,step,idx+pos+1,memo)
        memo[(pos,curstep)]=fin
        return fin

    def binarySearch(self,target,arr):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            if target>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        m={}
        res=self.helper(stones,0,0,m)
        return res
s=Solution()
# print(s.canCross([0,1,3,5,6,8,12,17]))
# print(s.canCross([0,1,2,3,4,8,9,11]))
# print(s.canCross([0,2]))
print(s.canCross([0,1,3,5,6,8,12]))
