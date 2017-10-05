class Solution(object):
    def nextPermutation(self, nums):
        length=len(nums)
        j=length-1
        while j>=1 and nums[j]<=nums[j-1]:
            j-=1
        if j==0:
            return self.reverse(nums,0,length-1)
        i=j-1
        j=length-1
        while j>i and nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        self.reverse(nums,i+1,length-1)
    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
s=Solution()
s.nextPermutation([3,2,1])