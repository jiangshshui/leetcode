from collections import OrderedDict
# class Solution(object):
#
#     def get_structure(self,s):
#         temp =OrderedDict()
#         s = list(s)
#         for index, s_ch in enumerate(s):
#             temp_list = []
#             if s_ch not in temp:
#                 temp_list.append(index)
#                 temp[s_ch] = temp_list
#             else:
#                 temp_list = temp.get(s_ch)
#                 temp_list.append(index)
#                 temp[s_ch] = temp_list
#         return temp
#     def isIsomorphic(self, s, t):
#         if len(s)!=len(t):
#             return False
#         m_s=self.get_structure(s)
#         m_t=self.get_structure(t)
#         l_s=[]
#         l_t=[]
#         for k,v in m_s.items():
#             l_s.append(v)
#         for k,v in m_t.items():
#             l_t.append(v)
#         return l_s == l_t


class Solution(object):
    def isIsomorphic(self, s, t):
        m1={}
        m2={}
        for i in range(len(s)):
            if m1.get(s[i],0)!=m2.get(t[i],0):
                return False
            m1[s[i]]=i+1
            m2[t[i]]=i+1
        return True

s=Solution()
print(s.isIsomorphic("paper","title"))

'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}
        used = {}
        for x,y in zip(s,t):
            if x not in mapping:
                if y not in used:
                    mapping[x] = y
                else:
                    return False
                used[y] = True
            elif mapping[x] != y:
                return False
        return True
'''