class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
s=Solution()
print(s.rangeBitwiseAnd(1,3))

'''
https://www.cnblogs.com/grandyang/p/4431646.html
'''