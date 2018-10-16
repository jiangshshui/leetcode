class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_position=[]
        for i,s in enumerate(S):
            if s==C:
                c_position.append(i)

        ans=[]
        i=0
        j=0
        while i<len(S):
            if j==len(c_position):
                ans.append(i-c_position[j-1])
                i+=1
            elif i<=c_position[j]:
                if j>=1:
                    ans.append(min(c_position[j]-i,i-c_position[j-1]))
                else:
                    ans.append(c_position[j] - i)
                i += 1
            else:
                j+=1
        return ans



if __name__=="__main__":
    s=Solution()
    print(s.shortestToChar("aaba","b"))