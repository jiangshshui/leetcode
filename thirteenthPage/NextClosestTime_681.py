class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        res=set()
        for i in range(24*60):
            for t in ["%02d:%02d"%divmod(i,60)]:
                if set(t)<=set(time):
                    res.add((t<=time,t))#true 表示第二天后,false 表示仍然和time是同一天
        return min(res)[1]
s=Solution()
print(s.nextClosestTime("19:34"))
