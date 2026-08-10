# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,num):
            if not node:
                return 0
            num=num*10+node.val  #we can combine the values of the nodes by multiplying the previous value by 10 and add the current node value
            if not node.left and not node.right: #if there onlt one node then we return that node value
                return num
            left=dfs(node.left,num)
            right=dfs(node.right,num)
            return left+right #add the num of left and right subtree and return the sum
        return dfs(root,0)