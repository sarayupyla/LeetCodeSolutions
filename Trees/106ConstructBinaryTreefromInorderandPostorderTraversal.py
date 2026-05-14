# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i  #store the values of inorder in indorder_map with their index values
        self.post_index = len(postorder) - 1 #initally the root value will be at the end in postorder
        def helper(left, right):
            if left > right: 
                return None
            root_val = postorder[self.post_index] #get the root value from postorder using post_index
            self.post_index -= 1 #decrease the post_index  to get next value cause the root value is at the end in postorder
            root = TreeNode(root_val)
            mid = inorder_map[root_val] #get the index of root value in inorder using inorder_map 
            root.right = helper(mid + 1, right) #we build the right subtree cause in post order while it goes from back itsrot->right->left
            root.left = helper(left, mid - 1)
            return root
        return helper(0, len(inorder) - 1)