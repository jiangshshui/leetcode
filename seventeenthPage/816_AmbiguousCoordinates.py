class Solution:
    def f(self,s):
        n=len(s)
        if n==0 or n>1 and s[0]=='0' and s[n-1]=='0':
            return []
        if n>1 and s[0]=='0':
            return ['0.'+s[1:]]
        if n==1 or s[n-1]=='0':
            return [s]
        res=[]
        res.append(s)
        for i in range(1,n):
            res.append(s[0:i]+"."+s[i:])
        return res

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S=S[1:-1]
        res=[]
        for i in range(len(S)):
            resA,resB=self.f(S[0:i]),self.f(S[i:])
            for a in resA:
                for b in resB:
                    res.append("("+a+", "+b+")")
        return res



s=Solution()
print(s.ambiguousCoordinates("(123)"))
# print(s.ambiguousCoordinates("(00011)"))
# print(s.ambiguousCoordinates("(0123)"))
# print(s.ambiguousCoordinates("(100)"))


