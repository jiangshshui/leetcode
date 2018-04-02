class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[0 for _ in range(rowIndex+1)]
        res[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                res[j]=res[j]+res[j-1]
        return res


s=Solution()
print(s.getRow(3))