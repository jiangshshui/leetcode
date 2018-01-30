class Solution(object):
    def isHappy(self, num):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        s.add(num)
        while num != 1:
            temp = []
            while num:
                a = num % 10
                temp.append(a)
                num //= 10
            for item in temp:
                num += item ** 2
            if num in s:
                return False
            s.add(num)
        return True