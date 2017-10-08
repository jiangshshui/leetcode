
# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """
#         if dividend==-2**31 and (divisor==-1 or divisor==1):
#             return -2**31 if divisor==1 else 2**31-1
#         isPositive=(dividend>0) is (divisor>0)
#         dividend,divisor=abs(dividend),abs(divisor)
#         digits=0
#         while divisor<=dividend:
#             divisor=divisor<<1
#             digits+=1
#         divisor=divisor>>digits
#         digits-=1
#         res=0
#         while digits>=0:
#             if dividend>=(divisor<<digits):
#                 dividend-=divisor<<digits
#                 res+=1<<digits
#             digits-=1
#         return res if isPositive else -res


class Solution:
# @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
s=Solution()
print(s.divide(80,3))