class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def mergeTrees(self, t1, t2):
#         if not t1 and not t2:
#             return None
#         ans=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
#         ans.left=self.mergeTrees(t1.left if t1 else None,t2.left if t2 else None)
#         ans.right=self.mergeTrees(t1.right if t1 else None,t2.right if t2 else None)
#         return ans

# class Solution(object):
#     def mergeTrees(self, t1, t2):
#         if not t1 and not t2:
#             return None
#         ans=TreeNode((t1.val if t1 else 0)+(t2.val if t2 else 0))
#         ans.left=self.mergeTrees(t1 and t1.left,t2 and t2.left)#如果t1 和 t1.left中有一个为None 结果几位None，否则对象为后一个
#         ans.right=self.mergeTrees(t1 and t1.right,t2 and t2.right)
#         return ans

class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 is None:return t2
        if t2 is None:return t1
        ans=t1
        ans.val=t1.val+t2.val
        ans.left=self.mergeTrees(t1.left,t2.left)
        ans.right=self.mergeTrees(t1.right,t2.right)
        return ans
