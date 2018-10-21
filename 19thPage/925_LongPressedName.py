class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i=0
        k=0
        while i<len(name):
            j=i+1
            while j<len(name):
                if name[j]==name[i]:
                    j+=1
                else:
                    break
            m=k
            while m<len(typed):
                if typed[m]==name[i]:
                    m+=1
                else:
                    break
            if j-i>m-k:
                return False
            i=j
            k=m
        return True



if __name__=="__main__":
    s=Solution()
    print(s.isLongPressedName("laiden","laiden"))
    print(s.isLongPressedName( "leelee","lleeelee"))
    print(s.isLongPressedName("saeed","ssaaedd"))