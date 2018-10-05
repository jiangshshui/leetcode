class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if A==B:
            if len(set(A))==len(A):
                return False
            else:
                return True
        s=[]
        for i,j in zip(A,B):
            if i!=j:
                s.append([i,j])
        if len(s)>2:
            return False

        return s[0]==s[1][::-1]



if __name__=="__main__":
    s=Solution()
    print(s.buddyStrings("aaaaaaabc","aaaaaaacb"))