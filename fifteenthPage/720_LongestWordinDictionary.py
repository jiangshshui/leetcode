# class Solution:
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         best=""
#         for word in words:
#             if len(word)<len(best) or (word>best and len(best)==len(word)):
#                 continue
#             valid=True
#             for i in range(len(word)-1):
#                 if word[:i+1] not in words:
#                     valid=False
#                     break
#             if valid:
#                 best=word
#         return best

# from functools import cmp_to_key
# class Solution:
#     def longestWord(self, words):
#         """
#         :type words: List[str]
#         :rtype: str
#         """
#         def my_sort(val1,val2):
#             if len(val1)!=len(val2):
#                 return len(val1)-len(val2)
#             else:
#                 return 1 if val1<=val2 else -1
#         words = sorted(words, key=cmp_to_key(my_sort), reverse=True)
#         #print(words)
#         best=""
#         for word in words:
#             valid=True
#             for i in range(len(word)-1):
#                 if word[:i+1] not in words:
#                     valid=False
#                     break
#             if valid:
#                 best=word
#                 break
#         return best


from functools import cmp_to_key
class Solution:
    def __init__(self):
        self.root={}


    def insert_word(self,word):
        work=self.root
        for ch in word:
            if ch not in work:
                work[ch]={}
            work=work[ch]
        work["end"]=True

    def search(self,word):
        work=self.root
        for ch in word:
            if ch in work:
                work=work[ch]
            else:
                return False
        if "end" in work:
            return True
        else:
            return False

    def my_cmp(self,v1,v2):
        if len(v1)!=len(v2):
            return len(v1)-len(v2)
        else:
            return 1 if v1<v2 else -1

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            self.insert_word(word)
        words=sorted(words,key=cmp_to_key(self.my_cmp),reverse=True)

        for word in words:
            valid = True
            for i in range(len(word)-1):
                if not self.search(word[:i+1]):
                    valid=False
                    break
            if valid:
                return word








if __name__=="__main__":
    s=Solution()
    print(s.longestWord(["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l","o","mwaqz","oi","ych","m","mwa"]))
    print("oiddm"<"mwaqz")