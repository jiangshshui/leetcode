class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        arr=[None]*len(S)
        r=""
        for i,s in enumerate(S):
            if not s.isalpha():
                arr[i]=s
            else:
                r+=s


        j=len(r)-1
        for i,c in enumerate(arr):
            if arr[i] is None:
                arr[i]=r[j]
                j-=1
        return "".join(arr)



if __name__=="__main__":
    s=Solution()
    print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))