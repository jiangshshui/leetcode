class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        ans=0
        i,j=0,len(people)-1
        while i<=j:
            ans+=1
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
        return ans


if __name__=="__main__":
    s=Solution()
    print(s.numRescueBoats([3,5,3,4],5))
    print(s.numRescueBoats([3,2,2,1],3))
    print(s.numRescueBoats([5,1,4,2],6))