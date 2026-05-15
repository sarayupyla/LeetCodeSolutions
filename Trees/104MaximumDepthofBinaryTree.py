# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        d=0
        while q:
            d+=1 #we increase the depth by 1 for each level 
            for i in range(len(q)):
                element=q.popleft()
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
        return d
       