'''
时间较长

class Solution(object):
    def moveZeroes(self, nums):
        length=len(nums)
        if length==0:
            return
        lasti=i=length-1
        while i>=0:
            if nums[i]==0:
                for j in range(i,lasti):
                    nums[j]=nums[j+1]
                nums[lasti]=0
                lasti=lasti-1
            i-=1
        return nums
'''

class Solution(object):
    def moveZeroes(self, nums):
        if nums == []:
            return
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        for i in range(len(nums) - pos):
            nums[-i-1]=0
        return nums
s=Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))



