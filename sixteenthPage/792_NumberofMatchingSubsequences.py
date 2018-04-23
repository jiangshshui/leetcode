class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        m={}
        res=0
        for word in words:
            temp=""
            start=0
            for s in word:
                temp+=s
                if temp in m:
                    start=m[temp]
                    continue
                index=S.find(s,start)
                if index==-1:
                    break
                else:
                    start=index+1
                    m[temp]=index+1
            if word in m:
                res+=1
        return res


s=Solution()
print(s.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"]))