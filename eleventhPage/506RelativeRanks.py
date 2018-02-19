class Solution(object):
    def findRelativeRanks(self, nums):
        m={}
        for index,num in enumerate(nums):
            m[num]=index
        m=sorted(m.items(),key=lambda x:x[0],reverse=True)
        print(m)
        res=["" for _ in range(len(nums))]
        for index,value in enumerate(m):
            if index==0:
                res[value[1]]="Gold Medal"
            elif index==1:
                res[value[1]] =  "Silver Medal"
            elif index==2:
                res[value[1]] =  "Bronze Medal"
            else:
                res[value[1]]=str(index+1)
        return res

s=Solution()
print(s.findRelativeRanks([5, 6, 7, 2, 1]))