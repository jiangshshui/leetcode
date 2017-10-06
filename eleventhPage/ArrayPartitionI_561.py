class Solution(object):
    def arrayPairSum(self, nums):
        # nums=sorted(nums)
        # length=len(nums)
        # total=0
        # for i in range(0,length,2):
        #     total+=nums[i]
        # return total
        return sum(sorted(nums)[::2])

s=Solution()
print(s.arrayPairSum([1,4,3,2]))
