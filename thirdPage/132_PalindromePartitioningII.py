class Solution:
    def minCut(self, s):
        n=len(s)
        dp=[[False for _ in range(n)]for _ in range(n)]
        d=[0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            d[i]=n-i-1
            for j in range(i,n):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    if j==n-1:
                        d[i]=0
                    else:
                        d[i]=min(d[i],d[j+1]+1)
        print(d)
        return d[0]

s=Solution()
print(s.minCut("abbab"))