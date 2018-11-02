from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        cnt=Counter(deck)
        vals=cnt.values()
        return reduce(gcd,vals)>=2




if __name__=="__main__":
    s=Solution()
    #print(s.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
    #print(s.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
    print(s.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))

