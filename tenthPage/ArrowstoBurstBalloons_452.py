class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)<=1:
            return len(points)
        points=sorted(points)
        start=points[0]
        count=1
        for item in points[1:]:
            if item[0]>=start[0] and item[0]<=start[1]:
                start=[max(item[0],start[0]),min(item[1],start[1])]
            else:
                start=item
                count+=1
        return count


s=Solution()
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))
print(s.findMinArrowShots([[1,2]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(s.findMinArrowShots([[77171087,133597895],[45117276,135064454],[80695788,90089372],[91705403,110208054],[52392754,127005153],[53999932,118094992],[11549676,55543044],[43947739,128157751],[55636226,105334812],[69348094,125645633]]))