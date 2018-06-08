from collections import OrderedDict
class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W!=0:
            return False
        m=OrderedDict()
        hand.sort()
        for card in hand:
            if card not in m:
                m[card]=1
            else:
                m[card]+=1

        for key in m.keys():
            if m[key]>0:
                for v in range(m[key]):
                    for step in range(W):
                        if key+step not in m or m[key+step]<=0:
                            return False
                        m[key+step]-=1
        return True

s=Solution()
print(s.isNStraightHand([8,8,9,7,7,7,6,7,10,6],2))