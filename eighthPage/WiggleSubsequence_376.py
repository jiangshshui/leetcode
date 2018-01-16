class Solution(object):
    def wiggleMaxLength(self, nums):
        i=0
        if len(nums)==0:
            return 0
        res=1
        result=[]
        while i<len(nums)-1:
            # if nums[i]==nums[i+1]:错误的分成了三段,其实只要分成两段就行了
            #     i+=1
            #     continue
            pre=nums[i]
            if nums[i]<nums[i+1]:
                while i+1<len(nums) and nums[i]<=nums[i+1]:
                    i+=1
            else:
                while i+1<len(nums) and nums[i]>=nums[i+1]:
                    i+=1
            if(nums[i]!=pre):
                res+=1
        return res

s=Solution()
print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))