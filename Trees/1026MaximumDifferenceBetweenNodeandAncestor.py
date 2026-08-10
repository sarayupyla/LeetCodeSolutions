# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,minimum,maximum):
            if not node:
                return 0
            ans=max(abs(node.val-minimum),abs(node.val-maximum)) #we have to find the ,maximum difference btw the nodeand its ancestor
            minimum=min(minimum,node.val) #update the min and max values of the ancestor nodes as we traverse down
            maximum=max(maximum,node.val)
            left=dfs(node.left,minimum,maximum)
            right=dfs(node.right,minimum,maximum)
            return max(ans,left,right) #return maximum difference found in left,right and current node
        return dfs(root,root.val,root.val)