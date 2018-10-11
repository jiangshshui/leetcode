from functools import reduce
# class Solution:
#     def shiftingLetters(self, S, shifts):
#         """
#         :type S: str
#         :type shifts: List[int]
#         :rtype: str
#         """
#         total_shifts=[0]
#         for i in range(len(shifts)-1,-1,-1):
#             total_shifts.append(shifts[i]+total_shifts[-1])
#
#         ans=""
#         for i,shifts_sum in enumerate(total_shifts[:0:-1]):
#             actual_shift=shifts_sum%26
#             ans+=chr(ord('a')+(ord(S[i])+actual_shift-ord('a'))%26)
#         return ans

import string
class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        letters = string.ascii_lowercase
        s = 0
        S = list(S)
        for i in range(len(S) - 1, -1, -1):
            s += shifts[i]
            S[i] = letters[(letters.find(S[i]) + s) % 26]
        return ''.join(S)



if __name__=="__main__":
    s=Solution()
    print(s.shiftingLetters("abc",[3,5,9]))
    # print(ord('a'))
    # print(ord('z'))