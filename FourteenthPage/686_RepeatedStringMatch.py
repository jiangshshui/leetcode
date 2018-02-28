class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        cnt=0
        temp=A
        while len(temp)<len(B):
            temp+=A
            cnt+=1
        A=temp
        for i in range(1,3):
            temp=A*i
            cnt+=1
            if temp.find(B)!=-1:
                return cnt
        return -1


s=Solution()
#print(s.repeatedStringMatch("abcd" ,"cdabcdab"))
print(s.repeatedStringMatch("bb" ,"bbbbbbb"))