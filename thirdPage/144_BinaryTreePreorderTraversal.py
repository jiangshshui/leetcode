class Solution(object):
    def preorderTraversal(self, root):
        res=[]
        stack=[]
        node=root
        while node or len(stack)!=0:
            if node!=None:
                res.append(node.val)
                stack.append(node.right)
                node=node.left
            else:
                node=stack.pop()
        return res


s=Solution()
s.preorderTraversal()