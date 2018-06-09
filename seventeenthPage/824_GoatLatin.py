class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels=('a','e','i','o','u','A','E','I','O','U')
        res=[]
        words=S.split()
        for index,word in enumerate(words):
            if word[0] in vowels:
                res.append(word+"ma"+'a'*index)
            else:
                res.append(word[1:]+word[0]+"ma"+'a'*(index+1))
        return " ".join(res)


s=Solution()
print(s.toGoatLatin("I speak Goat Latin"))
