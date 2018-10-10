class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        front_max=[0]*n
        left_max=[]

        for i in range(m):
            left_max.append(max(grid[i]))

        for i in range(n):
            for j in range(m):
                front_max[i]=max(front_max[i],grid[j][i])

        # print(front_max)
        # print(left_max)

        ans=0
        for i in range(m):
            for j in range(n):
                ans+=min(left_max[i],front_max[j])-grid[i][j]

        return ans


if __name__=="__main__":
    s=Solution()
    print(s.maxIncreaseKeepingSkyline([ [3, 0, 8, 4],
                                        [2, 4, 5, 7],
                                        [9, 2, 6, 3],
                                        [0, 3, 1, 0] ]))