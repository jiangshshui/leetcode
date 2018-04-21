class Solution:
    def calcContinues(self,S,start):
        j=start+1
        while j<len(S):
            if S[j]==S[start]:
                j+=1
            else:
                break
        return j-start
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res=0
        for word in words:
            j=i=0
            while i<len(word):
                if word[i]!=S[j]:
                    break
                else:
                    sameLenOfWord=self.calcContinues(word,i)
                    sameLenOfS=self.calcContinues(S,j)
                    if sameLenOfWord == sameLenOfS or (sameLenOfS>=3 and sameLenOfWord<=sameLenOfS):
                        i+=sameLenOfWord
                        j+=sameLenOfS
                    else:
                        break
            if i>=len(word) and j>=len(S):
                res+=1
        return res

s=Solution()
#print(s.expressiveWords("heeellooo",["hello", "hi", "helo"]))
print(s.expressiveWords("dddiiiinnssssssoooo",["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]))
print(s.expressiveWords("aaa",["aaaa"]))