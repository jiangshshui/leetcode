class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        length=len(M)
        visited=set()
        def dfs(i):
            for j,value in enumerate(M[i]):
                if value and j not in visited:
                    visited.add(j)
                    dfs(j)

        ans=0
        for i in range(length):
            if i not in visited:
                visited.add(i)
                dfs(i)
                ans+=1
        return ans

s=Solution()
M=[[1,1,0],
 [1,1,0],
 [0,0,1]]
print(s.findCircleNum(M))




'''
[[1,1,0],
 [1,1,1],
 [0,1,1]]
'''

