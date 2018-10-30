class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s=set()
        for email in emails:
            index_at=email.find("@")
            prefix=email[:index_at]
            prefix=prefix.replace(".","")
            index_plus=prefix.find("+")
            prefix=prefix[:index_plus]
            s.add(prefix+email[index_at:])
        return len(s)


if __name__=="__main__":
    s=Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))