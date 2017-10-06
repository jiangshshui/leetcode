class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # all=len(candies)
        # type_of_candy=set()
        # for candy in candies:
        #     type_of_candy.add(candy)
        # sorts=len(type_of_candy)
        # if sorts>=all//2:
        #     return all//2
        # else:
        #     return sorts
        return min(len(candies)//2,len(set(candies)))

s=Solution()
print(s.distributeCandies([1,1,2,2,3,3]))