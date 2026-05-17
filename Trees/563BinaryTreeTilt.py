# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt=0 
        def dfs(node):
            if not node:
                return 0
            leftsum=dfs(node.left) #traverse till the leaf node and get sum of left subtree
            rightsum=dfs(node.right) #traverse till the leaf and get sum of right subtree    
            return node.val+leftsum+rightsum #we return the sum of the current node and its left,right nodes to parent node
        dfs(root)
        return self.total_tilt 
