import itertools

class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same={x for i,x in enumerate(fronts) if x==backs[i]}
        ans=9999
        for x in itertools.chain(fronts,backs):
            if x not in same:
                ans=min(ans,x)

        return ans%9999


if __name__=="__main__":
    s=Solution()
    print(s.flipgame([1,2,2,3,7],[1,3,3,1,3]))