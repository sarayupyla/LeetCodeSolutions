# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(float(node.val))  #have to convert the node value to float to get decimal values
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sum=0
            for num in level: #each element of the level is added to sum and then avg is calculated
                sum+=num
                avg=sum/len(level) #divide the sum of the level by the number of elements in that level 
            ans.append(avg)  #append avg value to the ans list 
        return ans
