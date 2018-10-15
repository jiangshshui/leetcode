# class Solution:
#     def advantageCount(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         ans=[None for i in range(len(A))]
#         A.sort()
#         for i,b in enumerate(B):
#             l,r=0,len(A)-1
#             while l<=r:
#                 mid=(l+r)//2
#                 if A[mid]>B[i] and (mid==0 or A[mid-1]<=B[i]):
#                     ans[i] = A[mid]
#                     del A[mid]
#                     break
#                 elif A[mid]<=B[i]:
#                     l=mid+1
#                 elif A[mid]>B[i] and A[mid-1]>B[i]:
#                     r=mid
#
#         j=0
#         for i,a in enumerate(ans):
#             if a==None:
#                 ans[i]=A[j]
#                 j+=1
#         return ans


class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]

if __name__=="__main__":
    s=Solution()
    print(s.advantageCount([12,24,8,32],[13,25,32,11]))
    #print(s.advantageCount([2, 7, 11, 15],[1, 10, 4, 11]))
    #print(s.advantageCount([0], [0]))