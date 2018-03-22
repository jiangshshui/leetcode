class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def createBST(self,nums,left,right):
        if left>right:
            return None
        mid=left+(right-left)//2
        cur=TreeNode(nums[mid])
        cur.left=self.createBST(nums,left,mid-1)
        cur.right=self.createBST(nums,mid+1,right)
        return cur
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createBST(nums,0,len(nums)-1)


