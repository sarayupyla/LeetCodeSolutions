# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      def samet(p,q):
          if not p and not q: #if both left and right nodes are null then they are symmetric
            return True
          if not p or not q: #if any one of the left or right node is null then not symmetric
            return False
          if p.val!=q.val: #if both left and right nodes values are not same then not symmetric
            return False
          left=samet(p.left,q.right) #we check the left node of left subtree with right node of right subtree
          right=samet(p.right,q.left) #we check the right node of left subtree with left node of right subtree
          if left and right:#if both the left and right nodes are symmetric then we return true else false
            return True 
          else:
            return False
      return samet(root.left,root.right)
       
        