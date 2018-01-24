class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        #half = len(nums[::2]) - 1
        half=(len(nums)-1)//2
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        return nums

s=Solution()
print(s.wiggleSort([1,2,35,6,7]))
nums=[1,2,3,4,5,6,7,8]
print(nums[::2])
print(len(nums[::2]))
nums=[1,2,3,4,5,6,7]
print(nums[::2])
print(len(nums[::2]))
'''
如果一个数组的个数是偶数,则中间的数的index是length//2-1==(length-1)//2
如果一个数组的个数是奇数,则中间的数的index是length//2==(length-1)//2
如果数组A的A[::2]的个数是(length-1)//2

lenght=4 A=[1,2,3,4] A[::2]=[1,3] len(A[::2]) - 1=1   (length-1)//2=1
lenght=5 A=[1,2,3,4,5] A[::2]=[1,3,5] len(A[::2])-1=2 (length-1)//2=2
'''