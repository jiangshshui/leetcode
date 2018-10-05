class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        m=n=1
        #n 为reflection 的次数加1
        #m 为extend 的次数加1
        while m*p!=n*q:
            n+=1
            m=n*q//p

        if m%2==0 and n%2==1:
            return 0
        if m%2==1 and n%2==1:
            return 1
        if m%2==1 and n%2==0:
            return 2


'''
https://leetcode.com/problems/mirror-reflection/discuss/146336/Java-solution-with-an-easy-to-understand-explanation

如果m 为偶数,延伸了奇数次,延伸奇数次向下   延伸偶数次向上
如果n 为偶数数，反射了奇数次 达到左边     反射偶数次右边   

'''


if __name__=="__main__":
    s=Solution()
    print(s.mirrorReflection(2,1))