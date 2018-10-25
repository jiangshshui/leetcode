class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans

if __name__=="__main__":
    s=Solution()
    #print(s.smallestRangeII([0,10],2))
    print(s.smallestRangeII([1,3,6],3))#
    print(s.smallestRangeII([2,7,2],1))#3