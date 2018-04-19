class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        listA=list(A)
        listB=list(B)
        if listA==listB:
            return True
        k=0
        while k<len(listA):
            listA.append(listA[0])
            listA=listA[1:]
            if listA==listB:
                return True
            k+=1
        return False

s=Solution()
print(s.rotateString('abcde','cdeab'))