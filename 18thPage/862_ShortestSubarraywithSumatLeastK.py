from collections import deque
class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N=len(A)
        P=[0]
        for x in A:
            P.append(P[-1]+x)
        ans=N+1
        monoq=deque()
        for y,Py in enumerate(P):
            while monoq and Py<=P[monoq[-1]]:
                monoq.pop()

            while monoq and Py-P[monoq[0]]>=K:
                ans=min(ans,y-monoq.popleft())
            monoq.append(y)
        return ans if ans<N+1 else -1


if __name__=="__main__":
    s=Solution()
    # print(s.shortestSubarray([1],1))
    # print(s.shortestSubarray([1,2], 4))
    # print(s.shortestSubarray([2,-1,2], 3))
    print(s.shortestSubarray([84, -37, 32, 40, 95],167))