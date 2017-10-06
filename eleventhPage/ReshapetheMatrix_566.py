class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0])<r*c:
            return nums

        li=[j for i in nums for j in i]
        #countc=0
        res=[]
        #temp=[]
        # for item in li:
        #     temp.append(item)
        #     countc+=1
        #     if countc==c:
        #         res.append(temp)
        #         temp=[]
        #         countc=0
        index=0
        while index<len(li):
            res.append(li[index:index+c])
            index+=c
        return res

s=Solution()
#print(s.matrixReshape([[1,2],[3,4]],1,4))
print(s.matrixReshape([[1,2],[3,4]],4,1))

