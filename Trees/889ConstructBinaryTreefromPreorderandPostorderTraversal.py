# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_map={}
        for i in range(len(postorder)):
            postorder_map[postorder[i]]=i #store the values of postorder in postorder_map with their index values
        self.pre_index=0 #we have root val at index 0 of preorder
        def helper(left,right):
            if left>right:
                return None
            root_val=preorder[self.pre_index] #get the root value from preorder index 0
            self.pre_index+=1 #increment the index value 
            root=TreeNode(root_val)
            if left==right: #if we have only one element then return that root
                return root
            left_root=preorder[self.pre_index]  #the left root is the 1st index of preorder where we can find mid value in postorder
            mid=postorder_map[left_root]# we take mid value from left_root cause the 0th index of preorder is present at last of post order hance we increment the value and take as mid value in postorder
            root.left=helper(left,mid) #as the left value is already visited in preorder we can directly take mid value from postorder
            root.right=helper(mid+1,right-1) #we move mid+1 to right-1 because the lastvalue in postorder is the root value which is already visited in preorder
            return root
        return helper(0,len(postorder)-1)