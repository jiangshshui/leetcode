from collections import defaultdict
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        # word_in_A=defaultdict(int)
        # word_in_B=defaultdict(int)
        # for word in A.split():
        #     word_in_A[word]+=1
        #
        # for word in B.split():
        #     word_in_B[word]+=1
        #
        # ans=[]
        # for k,v in word_in_A.items():
        #     if v==1 and k not in word_in_B:
        #         ans.append(k)
        #
        # for k,v in word_in_B.items():
        #     if v==1 and k not in word_in_A:
        #         ans.append(k)

        words=A.split()+B.split()
        ans=[]
        for word,cnt in Counter(words).items():
            if cnt==1:
                ans.append(word)
        return ans


if __name__=="__main__":
    s=Solution()
    print(s.uncommonFromSentences("this apple is sweet","this apple is sour"))