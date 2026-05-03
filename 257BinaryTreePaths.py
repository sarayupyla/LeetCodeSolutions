# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def sol(node,path):
            if node== None: #if node is null means no node exist
                return
            path+=str(node.val) #add node val to path
            if node.left == None and node.right == None: #leaf node
                ans.append(path)  #add path to answer list
                return 
            sol(node.left,path +"->")  #towards left
            sol(node.right,path + "->") #towards right
        sol(root,"") #initially path is empty str and root is first node
        return ans
        