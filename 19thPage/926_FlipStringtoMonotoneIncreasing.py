class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        p=[0]
        N=len(S)
        for s in S:
            p.append(p[-1]+int(s))
        ans=[]
        for x in range(len(p)):
            ans.append(p[x]+(N-x)-(p[N]-p[x]))
        return min(ans)


if __name__=="__main__":
    s=Solution()
    print(s.minFlipsMonoIncr("010110"))
    print(s.minFlipsMonoIncr("00011000"))