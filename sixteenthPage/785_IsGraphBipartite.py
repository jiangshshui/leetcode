class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        colors=[-1 for _ in range(n)]
        for i in range(n):
            if colors[i]==-1 and not self.validColor(graph,colors,0,i):
                return False
        return True

    def validColor(self,graph,colors,color,node):
        if colors[node]!=-1:
            return colors[node]==color    #判断此节点是不是染的这种颜色,是return True，不是return False
        colors[node]=color
        for next in graph[node]:
            if not self.validColor(graph,colors,1-color,next):
                return False
        return True

s=Solution()
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))
print(s.isBipartite([[1,3], [0,2], [1,3], [0,2]]))