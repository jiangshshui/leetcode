#
# class Solution:
#
#     def min_list_by_indices(self,quiet,indices):
#         mini_q=quiet[indices[0]]
#         mini_node=indices[0]
#         for index in indices[1:]:
#             if mini_q>quiet[index]:
#                 mini_q=quiet[index]
#                 mini_node=index
#         return mini_node
#
#
#     def add_bigger_nodes(self,edges,index):
#         res=[]
#         if len(edges[index])==0:
#             return res
#         res.extend(edges[index])
#         for node in edges[index]:
#             res.extend(self.add_bigger_nodes(edges,node))
#         return res
#
#
#
#     def loudAndRich(self, richer, quiet):
#         """
#         :type richer: List[List[int]]
#         :type quiet: List[int]
#         :rtype: List[int]
#         """
#         length=len(quiet)
#         edges=[[] for i in range(len(quiet))]
#
#         for r in richer:
#             larger,small=r[0],r[1]
#             edges[small].append(larger)
#
#         print(edges)
#
#         bigger=[[i] for i in range(len(quiet))]
#
#         for i in range(len(quiet)):
#             bigger[i].extend(self.add_bigger_nodes(edges,i))
#
#         res=[]
#         for i in range(length):
#             res.append(self.min_list_by_indices(quiet,bigger[i]))
#
#         return res

import collections
class Solution(object):
    def loudAndRich(self, richer, quiet):
        m = collections.defaultdict(list)
        for i, j in richer:
            m[j].append(i)
        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] >= 0:
                return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]: res[i] = res[j]
            return res[i]

        for i in range(len(quiet)):
            dfs(i)
        return res

if __name__=="__main__":
    s=Solution()
    print(s.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],
                        [3,2,5,4,6,1,7,0]))


'''
[[0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [2], [3, 4, 5, 6], [4], [5], [6], [7, 3, 4, 5, 6]]
'''