class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m=len(A)
        n=len(A[0])
        res=0
        res+=m*(1<<(n-1))

        for j in range(1,n):
            same=0
            for i in range(m):
                if A[i][0]==A[i][j]:
                    same+=1
            res+=(1<<(n-j-1))*max(m-same,same)
        return res

'''
https://leetcode.com/problems/score-after-flipping-matrix/discuss/143812/
C++Java-From-Intuition-Un-optimized-code-to-Optimized-Code-with-Detailed-Explanation
'''

if __name__=="__main__":
    s=Solution()
    print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))