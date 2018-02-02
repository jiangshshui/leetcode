'''
时间较长,未过时。

class Solution(object):

    def findStart(self,indegrees,visited):
        for index,indegree in enumerate(indegrees):
            if indegree==0 and not visited[index]:
                visited[index]=True
                return index
        return -1

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees=[0 for _ in range(numCourses)]
        for connection in prerequisites:
            indegrees[connection[0]]+=len(connection[1:])
        visited=[False for _ in range(numCourses)]
        start=self.findStart(indegrees,visited)
        cnt=0
        while start!=-1:
            cnt+=1
            for connection in prerequisites:
                if start in connection[1:]:
                    indegrees[connection[0]]-=1
            start=self.findStart(indegrees,visited)
        if cnt==numCourses:
            return True
        return False
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=[[] for _ in range(numCourses)]
        visit=[0 for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i]==-1:
                return False
            if visit[i]==1:
                return True
            visit[i]=-1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i]=1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

s=Solution()
print(s.canFinish(3,[[2,0],[2,1]]))