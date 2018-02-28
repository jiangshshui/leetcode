'''
Accepted,效率低下
'''
# class Solution(object):
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         nodeNums=len(edges)
#         indegree={}
#         for i in range(1,nodeNums+1):
#             indegree[i]=0
#         for item in edges:
#             indegree[item[0]]+=1
#             indegree[item[1]]+=1
#
#         def findOneIndegree(indegree):
#             for key in indegree.keys():
#                 if indegree[key]==1:
#                     return key
#             return -1
#         def delLinksWithOneIndegree(oneIndegree,edges):
#             res=[]
#             for edge in edges:
#                 if edge[0]==oneIndegree or edge[1]==oneIndegree:
#                     continue
#                 res.append(edge)
#             return res
#
#         def modifyIndegrees(indegree,oneIndegree,edges):
#             for edge in edges:
#                 if edge[0]==oneIndegree or edge[1]==oneIndegree:
#                     indegree[edge[0]]-=1
#                     indegree[edge[1]]-=1
#
#         oneIndegree=findOneIndegree(indegree)
#         while(oneIndegree!=-1):
#             modifyIndegrees(indegree,oneIndegree,edges)
#             edges=delLinksWithOneIndegree(oneIndegree,edges)
#             oneIndegree=findOneIndegree(indegree)
#         return edges[-1]




# class Solution(object):
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """
#         d = {}  ## keeps track of parent node
#
#         def root(v):
#             if v not in d:
#                 return v
#             return root(d[v])
#
#         for x, y in edges:
#             left = root(x)
#             right = root(y)
#             if left == right:
#                 return [x, y]
#             else:
#                 d[left]=right



class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root={}
        def findRoot(index):
            if index not in root:
                return index
            else:
                return findRoot(root[index])
        for edge in edges:
            leftRoot=findRoot(edge[0])
            rightRoot=findRoot(edge[1])
            if leftRoot!=rightRoot:
                root[rightRoot]=leftRoot
            else:
                return edge


s=Solution()
#print(s.findRedundantConnection([[1,2], [1,3], [2,3]]))
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
print(s.findRedundantConnection([[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]))