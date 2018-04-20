class Solution:

    def dfs(self,start,end,interPath,allPath,graph):
        interPath.append(start)
        if start==end:
            allPath.append(list(interPath))
        for node in graph[start]:
            self.dfs(node,end,interPath,allPath,graph)
        interPath.pop()

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        length=len(graph)
        allPath=[]
        interPath=[]
        self.dfs(0,length-1,interPath,allPath,graph)
        return allPath

s=Solution()
print(s.allPathsSourceTarget([[1,2], [3], [3], []] ))


