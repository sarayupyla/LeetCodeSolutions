# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root]) #we use queue to store the node of each level 
        ans=[] #outside list to store final answer as we have list of list in output
        while q: #while queue is not empty we keep on traversing
            level=[]
            n=len(q)
            for i in range(n):
                node=q.popleft() #the element at the front will be poped and will be appended to the level list
                level.append(node.val) #inside list to store the value of each level
                if node.left:
                    q.append(node.left) #we add left child to the queue if its not null
                if node.right: 
                    q.append(node.right) #we add right child to queue is its not null
            ans.append(level) #at last we have to add all th elevels in the answer list 
        return ans