# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def topView(self, root):
        #your code goes here
        if not root:
            return []
        dic = {}
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            if col not in dic: #we add the value of the node to dic only if the col is not already present so that we can take onlt top most node val
                dic[col] = node.data 
            if node.left:
                q.append((node.left, col - 1)) #vertical traversal so to get left node we decrease the col value
            if node.right:
                q.append((node.right, col + 1)) #vertical traversal so to get right node we increase the col value
        result = []
        for i in sorted(dic): #we need sorted order of vertical traversal as output (left to right) 
            result.append(dic[i]) 
        return result