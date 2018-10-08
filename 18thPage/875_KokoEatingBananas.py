class Solution:

    def is_ok(self,piles,mid,H):
        return sum((p-1)//mid+1 for p in piles)<=H

    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        l,r=1,max(piles)
        while l<r:
            mid=(l+r)//2
            if not self.is_ok(piles,mid,H):
                l=mid+1
            else:
                r=mid
        return l

if __name__=="__main__":
    s=Solution()
    print(s.minEatingSpeed())
