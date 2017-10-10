class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length=len(triangle)
        minium=triangle[-1]
        if length<=1:
            return minium[0]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                minium[j]=triangle[i][j]+min(minium[j],minium[j+1])
        return minium[0]

s=Solution()
print(s.minimumTotal([[2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]))