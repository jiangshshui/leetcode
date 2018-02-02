'''
超时

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        i=0
        secret=list(secret)
        guess=list(guess)
        cntA=0
        cntB=0
        while i<len(secret):
            if secret[i]==guess[i]:
                cntA+=1
                guess[i]=secret[i]='#'
            i+=1
        i=j=0
        while i<len(secret):
            if secret[i]=='#':
                i+=1
                continue
            while j<len(guess):
                if secret[i]==guess[j]:
                    cntB+=1
                    guess[j]="#"
                    break
                j+=1
            j=0
            i+=1
        return str(cntA)+"A"+str(cntB)+"B"
'''

'''

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        m_secret={}
        m_guess={}
        for ele in secret:
            m_secret[ele]=0
            m_guess[ele]=0
        for ele in guess:
            m_guess[ele]=0
            m_secret[ele]=0
        cntBull=cntCows=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                cntBull+=1
            else:
                m_secret[secret[i]]+=1
                m_guess[guess[i]]+=1
        for element in m_secret:
            cntCows+=min(m_guess[element],m_secret[element])
        return str(cntBull)+"A"+str(cntCows)+"B"
'''

# class Solution(object):
#     def getHint(self, secret, guess):
#         """
#         :type secret: str
#         :type guess: str
#         :rtype: str
#         """
#         m_secret={}
#         m_guess={}
#         for ele in secret:
#             m_secret[ele]=0
#             m_guess[ele]=0
#         for ele in guess:
#             m_guess[ele]=0
#             m_secret[ele]=0
#         cntBull=cntCows=0
#         for i in range(len(secret)):
#             if secret[i]==guess[i]:
#                 cntBull+=1
#             else:
#                 m_secret[secret[i]]+=1
#                 m_guess[guess[i]]+=1
#         for element in m_secret:
#             cntCows+=min(m_guess[element],m_secret[element])
#         return str(cntBull)+"A"+str(cntCows)+"B"

class Solution(object):
    def getHint(self, secret, guess):
        cntBull=cntCows=0
        numbers=[0 for i in range(10)]
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                cntBull+=1
            else:
                if numbers[int(secret[i])]<0:
                    cntCows+=1
                if numbers[int(guess[i])]>0:
                    cntCows+=1
                numbers[int(secret[i])]+=1
                numbers[int(guess[i])]-=1
        return str(cntBull)+"A"+str(cntCows)+"B"
s=Solution()
print(s.getHint("1123","0111"))