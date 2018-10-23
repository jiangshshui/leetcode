class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # if len(A)==1:
        #     return 0
        minmum=min(A)
        maxmum=max(A)
        K=K if K>=0 else -K
        return 0 if maxmum-K-(minmum+K)<0 else maxmum-K-(minmum+K)


if __name__=="__main__":
    s=Solution()
    print(s.smallestRangeI( [1], K = 0))