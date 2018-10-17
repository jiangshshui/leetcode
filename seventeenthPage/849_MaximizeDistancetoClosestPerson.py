class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seated=[]
        for i,seat in enumerate(seats):
            if seat!=0:
                seated.append(i)

        ans=0
        ans=max([ans,seated[0]-0,len(seats)-1-seated[-1]])
        for i in range(len(seated)-1):
            mid=(seated[i+1]-seated[i])//2
            ans=max(ans,mid)

        return ans



if __name__=="__main__":
    s=Solution()
    print(s.maxDistToClosest([1,0,0,0,1,0,1]))
    print(s.maxDistToClosest([1,0,0,0]))