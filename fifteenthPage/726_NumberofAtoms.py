class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        counts,_=self.helper(formula,0)
        counts=sorted(counts.items(),key=lambda x:x[0][0])
        ans=""
        for k,v in counts:
            if v!=1:
                ans+=k+str(v)
            else:
                ans+=k
        return ans

    def helper(self,s,i):
        counts={}
        while i!=len(s):
            if s[i]=='(':
                tempcounts,i=self.helper(s,i+1)
                num,i=self.get_count(s,i)
                for k,v in tempcounts.items():
                    if k not in counts:
                        counts[k]=v*num
                    else:
                        counts[k] += v * num
            elif s[i]==")":
                return counts,i+1
            else:
                name,i=self.get_name(s,i)
                num,i=self.get_count(s,i)
                if name not in counts:
                    counts[name]=num
                else:
                    counts[name]+=num
        return counts,i


    def get_name(self,s,i):
        name=""
        while i<len(s) and s[i].isalpha() and (name =="" or s[i].islower()):
            name+=s[i]
            i+=1
        return name,i

    def get_count(self,s,i):
        count_str=""
        while i<len(s) and s[i].isdigit():
            count_str+=s[i]
            i+=1
        return 1 if len(count_str) is 0 else int(count_str),i





if __name__=="__main__":
    s=Solution()
    print(s.countOfAtoms("Mg(OH)2"))
    print(s.countOfAtoms("K4(ON(SO3)2)2"))
    print(s.countOfAtoms("H11He49NO35B7N46Li20"))