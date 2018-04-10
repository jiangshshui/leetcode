class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        minDistance=abs(target[0])+abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0]-target[0])+abs(ghost[1]-target[1])<minDistance:
                return False
        return True


s=Solution()
print(s.escapeGhosts())