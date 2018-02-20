class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        step=[(-1,1),(1,-1)]#斜向上  斜向下
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        i=j=0
        cnt=1
        up=True
        res.append(matrix[0][0])
        change=True
        while cnt<m*n:
            if up:
                targeti=i+step[0][0]
                targetj=j+step[0][1]
                if targeti<0 and targetj<n:
                    targeti=0
                    change = True
                elif targeti<0 and targetj>=n:
                    targeti=1
                    targetj=n-1
                    change = True
                elif targetj>=n:
                    targeti=i+1
                    targetj=n-1
                    change = True
                else:
                    change=False
            if not up:
                targeti=i+step[1][0]
                targetj=j+step[1][1]
                if targetj < 0 and targeti >= m:
                    targeti=m-1
                    targetj=j+1
                    change=True
                elif targetj < 0 and targeti<m:
                    targetj = 0
                    change = True
                elif targeti>=m:
                    targeti = m - 1
                    targetj = j+1
                    change = True
                else:
                    change=False
            if change:
                up=not up
            i,j=targeti,targetj
            res.append(matrix[i][j])
            cnt+=1
        return res

s=Solution()
print(s.findDiagonalOrder([[ 1, 2, 3 ],
                            [ 4, 5, 6 ],
                            [ 7, 8, 9 ],
                           [10,11,12]]))