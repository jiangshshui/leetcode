class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def traverse(self,res):
        if not self:
            return
        if self.left:
            self.left.traverse(res)
        res.append(self.val)
        if self.right:
            self.right.traverse(res)

    def __str__(self):
        root=[]
        self.traverse(root)
        return str(root)

def createBSTFromList(nums):
    root = None
    for num in nums:
        root=insertTree(root,num)
    return root


def insertTree(root,num):
    if not root:
        root=TreeNode(num)
    elif num<root.val:
        root.left=insertTree(root.left,num)
    else:
        root.right=insertTree(root.right,num)
    return root


class SwapTwoTreeNode():
    def __init__(self,first,second):
        self.first=first
        self.second=second
        self.firstNode=None
        self.secondNode=None
    def swap(self,root):
        # firstNode=None
        # secondNode=None
        def traverse(root, i):
            if not root:
                return i
            i=traverse(root.left, i)
            i += 1
            if i ==self.first:
                self.firstNode=root
            if i==self.second:
                self.secondNode=root
            i=traverse(root.right,i)
            return i
        traverse(root,0)
        print(self.firstNode,self.secondNode)
        self.firstNode.val,self.secondNode.val=self.secondNode.val,self.firstNode.val
        return root

# def traverse(root,res):
#     if not root:
#         return
#     traverse(root.left,res)
#     res.append(root.val)
#     traverse(root.right,res)


# root=createBSTFromList([30,20,50,40,70,90,80])
# print(root)


