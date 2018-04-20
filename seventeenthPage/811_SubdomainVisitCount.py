class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        m={}
        for item in cpdomains:
            times,website=item.split()
            website_level=website.split('.')
            for i in range(len(website_level)):
                combine=""
                for j in range(i,len(website_level)):
                    if j==i:
                        combine+=website_level[j]
                    else:
                        combine+="."+website_level[j]
                if combine not in m:
                    m[combine]=int(times)
                else:
                    m[combine]+=int(times)
        res=[]
        for key,value in m.items():
            res.append(str(value)+" "+key)
        return res



s=Solution()
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))