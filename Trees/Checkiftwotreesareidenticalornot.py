# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        #your code goes here
        if not p and not q:# if both trees are empty then they are identical 
            return True
        if not p or not q:# if only one tree is empty then they are not identical
            return False
        if p.val!=q.val:# if the values of the current nodes are different then they are not identical
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    