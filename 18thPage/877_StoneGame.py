class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        Alex=[]
        Lee=[]
        begin=0
        end=len(piles)-1
        while len(Alex)!=len(piles)//2:
            if piles[begin]==max(piles[begin],piles[end]):
                Alex.append(piles[begin])
                begin+=1
            else:
                Alex.append(piles[end])
                end-=1
            if piles[begin]==min(piles[begin],piles[end]):
                Lee.append(piles[begin])
                begin+=1
            else:
                Lee.append(piles[end])
                end-=1
        return sum(Alex)>sum(Lee)
    
s=Solution()
print(s.stoneGame([3,7,2,3]))