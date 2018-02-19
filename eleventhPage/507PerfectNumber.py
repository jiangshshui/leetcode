class Solution(object):
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        i=2
        total=1
        while i*i<=num:
            if num%i==0:
                total+=(i+num/i)
            if i*i==num:
                total-=i
            if total>num:
                return False
            i+=1
        return total==num
print(Solution().checkPerfectNumber(28))