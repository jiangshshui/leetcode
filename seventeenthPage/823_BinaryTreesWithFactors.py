class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        MOD=10**9+7
        dp=[1 for i in range(len(A))]
        index={v:i for i,v in enumerate(A)}
        for i,a in enumerate(A):
            for j in range(i):
                if A[i]%A[j]==0:
                    right=A[i]//A[j]
                    if right in index:
                        dp[i]+=dp[j]*dp[index[right]]
                        dp[i]=dp[i]%MOD

        return sum(dp)%MOD



if __name__=="__main__":
    s=Solution()
    print(s.numFactoredBinaryTrees([1,2,3]))
    print(8%4)