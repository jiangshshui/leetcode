import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        end=int(math.sqrt(n)+1)
        isPrime=[True for _ in range(n)]
        for i in range(2,end):
            if isPrime[i]:
                for j in range(i**2,n,i):
                    isPrime[j]=False
        for prime in isPrime[2:]:
            if prime:
                cnt+=1
        return cnt

s=Solution()
print(s.countPrimes(2))