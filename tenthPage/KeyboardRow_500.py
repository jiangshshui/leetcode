class Solution(object):
    def findWords(self, words):
        mappings={
            1:'qwertyuiop',
            2:"asdfghjkl",
            3:"zxcvbnm"
        }
        flag=True
        res=[]
        for word in words:
            wordTemp=word.lower()
            if wordTemp[0] in mappings[1]:
             location=1
            elif wordTemp[0] in mappings[2]:
             location=2
            else:
             location=3
            for ch in wordTemp:
                if ch not in mappings[location]:
                    flag=False
                    break
            if flag:
                res.append(word)
            flag=True
        return res


s=Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))