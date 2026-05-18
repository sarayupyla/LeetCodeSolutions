# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(node,level):
            if not node:
                return 
            if level==len(ans):
                ans.append(node.val)
            dfs(node.left,level+1) #we traverse from root left right so that we can get first left most node value in each level
            dfs(node.right,level+1)
        dfs(root,0)
        return ans