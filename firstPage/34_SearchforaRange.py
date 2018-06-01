class Solution:
    def binary_search(self,nums,target,low,high):
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        index=self.binary_search(nums,target,0,len(nums)-1)
        if index==-1:
            return [-1,-1]
        start=index
        while start>=0:
            if nums[start]!=target:
                break
            start-=1

        end=index
        while end<len(nums):
            if nums[end]!=target:
                break
            end+=1
        return [start+1,end-1]

s=Solution()
print(s.searchRange([5,7,7,8,8,10],8))
print(s.searchRange([5,7,7,8,8,10],6))
print(s.searchRange([5,7,7,8,8,10],5))
print(s.searchRange([2,2],3))