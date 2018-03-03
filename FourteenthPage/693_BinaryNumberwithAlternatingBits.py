class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res=[]
        while n:
            last=n&1
            res.append(last)
            n>>=1
        i=0
        if len(res)==1:
            return True
        for i in range(len(res)-1):
            if res[i]-res[i+1]==1 or res[i]-res[i+1]==-1:
                continue
            else:
                return False
        if i==len(res)-2:
            return True

s=Solution()
print(s.hasAlternatingBits(1))