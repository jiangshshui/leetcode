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


# def traverse(root,res):
#     if not root:
#         return
#     traverse(root.left,res)
#     res.append(root.val)
#     traverse(root.right,res)


# root=createBSTFromList([30,20,50,40,70,90,80])
# print(root)


