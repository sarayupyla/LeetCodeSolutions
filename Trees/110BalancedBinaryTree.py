# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def help(root):
            if not root:
               return 0
            lh=help(root.left) #to traverse left subtree and get height of the left subtree
            rh=help(root.right) #to traverse right and get height
            if lh==-1 or rh==-1: #if any one subtree is unbalanced then return false 
                return -1
            if abs(lh-rh)>1: #if the difference of height is more than 1 then its unbalanced
                return -1
            return 1+max(lh,rh) #we calculate height of the tree 
        return help(root)!=-1 #if value is -1 then unbalanced else balanced
                
            
            
            
        