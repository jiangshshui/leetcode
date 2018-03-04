from collections import Counter
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        for index,num in enumerate(nums):
            if num not in m:
                m[num]=(1,index,index)
            else:
                replicates,first,last=m[num]
                replicates+=1
                last=index
                m[num]=(replicates,first,last)

        values=m.values()
        maxReplicate=max(values)[0]
        smallest=len(nums)
        for value in values:
            if value[0]==maxReplicate and value[2]-value[1]+1<smallest:
                smallest=value[2]-value[1]+1
        return smallest





s=Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1]))