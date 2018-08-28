class Solution:

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        ans = 0
        l = r = -1
        for x, y in intervals:
            if x > r:
                ans += 2
                l, r = y - 1, y
            elif l < x <= r:
                ans += 1
                l, r = r, y
            else:
                pass
        return ans
s=Solution()
print(s.intersectionSizeTwo( [[33,44],[42,43],[13,37],[24,33],[24,33],[25,48],[10,47],[18,24],[29,37],[7,34]]))