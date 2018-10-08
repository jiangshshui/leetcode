class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        top=0
        front=0
        side=0
        for i in range(m):
            side+=max(grid[i])
            for j in range(n):
                if grid[i][j]!=0:
                    top+=1

        for j in range(n):
            max_col=0
            for i in range(m):
                max_col=max(max_col,grid[i][j])
            front+=max_col


        return top+front+side


if __name__=="__main__":
    s=Solution()
    print(s.projectionArea([[2]]))
    grid=[[1,2],
          [3,4],
          [5,6]]
    print(list(zip(*grid)))