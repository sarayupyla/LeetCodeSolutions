# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def bottomView(self, root):
        #your code goes here
        if not root:
            return [] 
        dict={}
        queue=deque([(root,0)])
        while queue:
            node,col=queue.popleft()
            dict[col]=node.data
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        res=[]
        for i in sorted(dict):
            res.append(dict[i])
        return res