class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        visited=[[False for j in range(n)] for i in range(m)]
        steps=[(-1,0),(1,0),(0,-1),(0,1)]
        self.area=0
        res=0
        def travel(r,c):
            visited[r][c]=True
            for step in steps:
                tr,tc=r+step[0],c+step[1]
                if tr<0 or tr>=m or tc<0 or tc>=n:
                    continue
                elif not visited[tr][tc] and grid[tr][tc]:
                    self.area+=1
                    travel(tr,tc)

        for r in range(m):
            for c in range(n):
                self.area=0
                if grid[r][c] and not visited[r][c]:
                    self.area+=1
                    travel(r,c)
                res=max(res,self.area)
        return res

s=Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))