class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        return n&n-1==0

'''
如果一个整数是2的n次方,那么它的二进制数的最高位是1,其他的位数都必然是0
n-1 它的二进制位数都是11..111,相与必为零。。
'''

        # if 2**31%n==0:
        #     return True
        # else:
        #     return False
s=Solution()
print(s.isPowerOfTwo(4))