# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        dict={}
        queue=deque([(root,0,0)])#node,row,col
        while queue:
            node,row,col=queue.popleft()
            if col not in dict:
                dict[col]=[]
            dict[col].append((row,node.val))
            if node.left:
                queue.append((node.left,row+1,col-1))#towards left we decrease col val and row is similar to level order so we increase down the traversal
            if node.right:
                queue.append((node.right,row+1,col+1)) #towards right we increase col val
        res=[]
        for i in sorted(dict): #sorted only col in the dict
            temp=sorted(dict[i]) #we sort the row and val of that particular col in the dict so we get correct VOT
            res.append([v for r,v in temp]) #take only val from the sorted list in temp and add that val to res list
        return res