class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total=0
        if not timeSeries:
            return 0
        for index,time in enumerate(timeSeries[:-1]):
            if time+duration<=timeSeries[index+1]:
                total+=duration
            else:
                total+=timeSeries[index+1]-timeSeries[index]
        return total+duration

s=Solution()
print(s.findPoisonedDuration([1,4], 2))
print(s.findPoisonedDuration([1,3,5,7,9,11,13,15],3))