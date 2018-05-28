class Solution:
    def decide(self,grid,i,j):
        for row in range(i-1,i+2):
            for col in range(j-1,j+2):
                if grid[row][col]<0 or grid[row][col]>=10:
                    return False

        for row in range(i-1,i+2):
            if sum(grid[row][j-1:j+2])!=15:
                return False
        total=0
        for col in range(j-1,j+2):
            total+=grid[i-1][col]+grid[i][col]+grid[i+1][col]
            if total!=15:
                return False
            total=0
        return True
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==5 and i-1>=0 and j-1>=0 and i+1<len(grid) and j+1<len(grid[0]):
                    l.append((i,j))

        for i,j in l:
            if self.decide(grid,i,j):
                res+=1

        return res


s=Solution()
# print(s.numMagicSquaresInside( [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]))

print(s.numMagicSquaresInside([[1,8,6],[10,5,0],[4,2,9]]))

'''
[[1,8,6],
[10,5,0],
[4,2,9]]
'''