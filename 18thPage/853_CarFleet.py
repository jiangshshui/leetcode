class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time=[]
        comb=list(zip(position,speed))
        comb=sorted(comb,key=lambda x:x[0],reverse=True)
        for p,s in comb:
            time.append((target-p)/s)

        ans=len(position)
        pre=0
        for i in range(len(position)):
            if time[i]<=pre:
                ans-=1
            else:
                pre=time[i]

        return ans




if __name__=="__main__":
    s=Solution()
    print(s.carFleet(12, [10,8,0,5,3],[2,4,1,1,3]))
    print(s.carFleet(10,[2, 4],[3, 2]))

