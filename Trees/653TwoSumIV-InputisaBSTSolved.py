# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s=set()
        def dfs(node):
            if not node:
                return False
            need=k-node.val #we need this value to get the sum k
            if need in s:
                return True #if we have the need value in set then we got pair or nodes whose sum is k
            s.add(node.val)
            return dfs(node.left) or  dfs(node.right)
        return dfs(root)