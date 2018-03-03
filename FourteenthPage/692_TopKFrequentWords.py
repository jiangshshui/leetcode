from functools import cmp_to_key
class Solution(object):
    def topKFrequent(self, words, k):
        from collections import Counter
        freq={}
        counter=Counter(words)
        for word,cnt in counter.items():
            if cnt not in freq:
                freq[cnt]=[]
            freq[cnt].append(word)
        res=[]
        for i in range(len(words),0,-1):
            if i in freq:
                for word in freq[i]:
                    res.append((word,i))

        key=cmp_to_key(lambda a,b:b[1]-a[1] if a[1]!=b[1] else (-1 if a[0]<b[0] else 1))
        res.sort(key=key)
        return [el[0] for el in res[:k]]

s=Solution()
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))