class Solution(object):
    def knightDialer(self, N):
        mod=10**9+7
        next_step=((4,6),(6,8),(4,8),(7,9),(0,3,9),(),(0,1,7),(2,6),(1,3),(2,4))
        dp=[1]*10
        for i in range(N-1):
            dp_new=[0]*10
            for i,v in enumerate(dp):
                for next in next_step[i]:
                    dp_new[next]+=v
                    dp_new[next]%=mod

            dp=dp_new
        return sum(dp)%mod


if __name__=="__main__":
    s=Solution()
    print(s.knightDialer(3))