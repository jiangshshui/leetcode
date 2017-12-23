from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        res=[]
        for key,value in d.items():
            res.append(value)
        return res




s=Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))