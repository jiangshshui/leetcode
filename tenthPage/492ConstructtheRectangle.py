import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L=int(math.sqrt(area))
        while L:
            if area%L==0:
                return [area//L,L]
            L-=1

s=Solution()
print(s.constructRectangle(9999992))
