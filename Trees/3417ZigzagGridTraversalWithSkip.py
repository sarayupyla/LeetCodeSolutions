class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result=[]
        take=True
        for i in range(len(grid)):
            if i %2==0: #for even index we take the row as it is and for odd index we reverse the row
                row=grid[i]
            else:
                row=grid[i][::-1]
            for num in row:
                if take: #we take the value and append to result and the next value in the grid is skipped so we reverse the odd index grid values
                    result.append(num)
                take=not take #alternate values are taken 
        return result