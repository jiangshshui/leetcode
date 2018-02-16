class Solution(object):
    def operate(self,nums,start,end):
        while start<end:
            temp=nums[end]
            nums[end]=nums[start]
            nums[start]=temp
            start+=1
            end-=1
    def rotate(self, nums, k):
        k=k%len(nums)
        self.operate(nums,0,len(nums)-1)
        self.operate(nums,0,k-1)
        self.operate(nums,k,len(nums)-1)
        return nums

s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))