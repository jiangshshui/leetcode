import math
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<2:
            return 0
        left=0
        right=len(height)-1
        maxArea=0
        while left<right:
            area=(right-left)*math.min(height[left],height[right])
            if maxArea<area:
                maxArea=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea





