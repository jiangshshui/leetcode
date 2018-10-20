class Solution:
    def transform(self,version):
        if len(version)==0:
            return []
        version=version.split(".")
        return [int(x) for x in version]
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i=0
        digit1=self.transform(version1)
        digit2=self.transform(version2)
        while i<len(digit1) and i<len(digit2):
            if digit1[i]<digit2[i]:
                return -1
            elif digit1[i]>digit2[i]:
                return 1
            else:
                i+=1
        # if len(digit1)==len(digit2):
        #     return 0
        # if len(digit1)<len
        return 0 if sum(digit1[i:len(digit1)])==sum(digit2[i:len(digit2)]) else 1 if sum(digit1[i:len(digit1)])>sum(digit2[i:len(digit2)]) else -1

if __name__=="__main__":
    s=Solution()
    print(s.compareVersion("0.1","1.1"))
    print(s.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
    print(s.compareVersion(version1 = "1.0.1", version2 = "1"))
    print(s.compareVersion("1.0","1"))