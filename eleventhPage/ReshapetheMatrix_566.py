class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums)*len(nums[0])<r*c:
            return nums

        li=[j for i in nums for j in i]
        res=[]
        index=0
        while index<len(li):
            res.append(li[index:index+c])
            index+=c
        return res

s=Solution()
print(s.matrixReshape([[1,2],[3,4]],4,1))

