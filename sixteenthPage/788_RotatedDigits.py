class Solution:
    # def __init__(self):
    #     self.rotate2Others={2:5,5:2,6:9,9:6}
    #     self.cannotRotate=(3,4,7)
    #
    # def canRotated(self,num):
    #     temp=num
    #     acc=0
    #     base=1
    #     while temp:
    #         last=temp%10
    #         if last in self.cannotRotate:
    #             return False
    #         elif last in self.rotate2Others:
    #             last=self.rotate2Others[last]
    #         temp//=10
    #         acc=acc+last*base
    #         base*=10
    #     if acc==num:
    #         return False
    #     return True
    # def rotatedDigits(self, N):
    #     """
    #     :type N: int
    #     :rtype: int
    #     """
    #     cnt=0
    #     for i in range(1,N+1):
    #         if self.canRotated(i):
    #             cnt+=1
    #     return cnt

    def rotatedDigits(self, N):
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = list(map(int, str(N)))
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7 ** (len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3 ** (len(N) - i - 1)
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))


s=Solution()
print(s.rotatedDigits(99))

'''
http://www.frankmadrid.com/ALudicFallacy/2018/02/28/rotated-digits-leet-code-788/
'''