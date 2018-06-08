class Solution:

    def smaller(self,A):
        res=[0 for _ in range(len(A))]
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                res[i]=res[i-1]+1
        return res


    def larger(self,A):
        res=[0 for _ in range(len(A))]
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                res[i]=res[i+1]+1
        return res

    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res_small=self.smaller(A)
        res_larger=self.larger(A)
        max=0
        for i in range(len(A)):
            if res_larger[i] != 0 and  res_small[i] != 0 and res_larger[i] + res_small[i] > max:
                max=res_larger[i]+res_small[i]
        if max==0:
            return 0
        else:
            return max+1



s=Solution()
print(s.longestMountain([2,3]))