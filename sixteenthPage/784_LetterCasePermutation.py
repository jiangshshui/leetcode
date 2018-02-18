class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        num_of_letters=0
        for ch in S:
            if ch.isalpha():
                num_of_letters+=1
        if num_of_letters==0:
            return [S]
        res=[]
        for i in range(2**num_of_letters):
            bins=list(bin(i))[2:]
            if len(bins)<num_of_letters:
                #bins.insert(0,'0'*(num_of_letters-len(bins)))
                bins=['0']*(num_of_letters-len(bins))+bins
            temp=""
            j=0
            for isbin in bins:
                if isbin=='1':
                    while not S[j].isalpha():
                        temp += S[j]
                        j+=1
                    temp+=S[j].upper()
                if isbin=='0':
                    while not S[j].isalpha():
                        temp += S[j]
                        j+=1
                    temp+=S[j].lower()
                j+=1
            if j!=len(S):
                temp+=S[j:]
            res.append(temp)
        return res



s=Solution()
# print(s.letterCasePermutation("12345"))
# print(s.letterCasePermutation("a1b2"))
print(s.letterCasePermutation("mQe"))