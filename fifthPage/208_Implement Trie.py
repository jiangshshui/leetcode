# from collections import defaultdict
# class Node():
#     def __init__(self,ch):
#         self.ch=ch
#         self.is_word=False
#         self.d=defaultdict(Node)

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        work=self.root
        for ch in word:
            if ch in work:
                work=work[ch]
            else:
                work[ch]={}
                work=work[ch]
        work["end"]=True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        work=self.root
        hasword=True
        for ch in word:
            if ch in work:
                work = work[ch]
                continue
            else:
                hasword=False
                break
        if hasword and "end" not in work:
            hasword=False
        return hasword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        work = self.root
        hasprefix = True
        for ch in prefix:
            if ch in work:
                work=work[ch]
                continue
            else:
                hasprefix = False
                break
        return hasprefix


if __name__=="__main__":
    s=Trie()
    print(s.insert("a"))
    print(s.search("a"))
    print(s.startsWith("a"))