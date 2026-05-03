# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        level=0
        while q:
            size=len(q)
            if level%2==0: #even level
                prev=float("-inf")  #increasing order
            else:
                prev=float("inf")  #decreasing order
            for i in range(size):
                node=q.popleft()  #to get current node
                val=node.val      #to get value of current node
                if level%2==0:    #even level
                    if val%2==0 or val<=prev:   #val should not be even or decresing order
                        return False
                else:
                    if val%2!=0 or val>=prev: #val should not be odd or increasing order
                        return False
                prev=val
                if node.left:
                    q.append(node.left)  
                if node.right:
                    q.append(node.right)
            level+=1    
        return True