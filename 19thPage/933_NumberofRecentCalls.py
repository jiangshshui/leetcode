import collections
class RecentCounter:
    def __init__(self):
        self.q=collections.deque()


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0]<t-3000:
            self.q.popleft()
        return len(self.q)


if __name__=="__main__":
    s=RecentCounter()
    s.ping()
