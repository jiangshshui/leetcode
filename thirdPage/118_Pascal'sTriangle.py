class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows<=0:
            return []
        res=[[1]]
        for num in range(1,numRows):
            tmp=[]
            for index in range(len(res[num-1])+1):
                if index-1<0:
                    tmp.append(res[num-1][index])
                elif index>=len(res[num-1]):
                    tmp.append(res[num-1][index-1])
                else:
                    tmp.append(res[num-1][index-1]+res[num-1][index])
            res.append(tmp)
        return res
s=Solution()
print(s.generate(5))