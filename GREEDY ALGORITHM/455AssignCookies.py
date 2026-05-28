class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        c=0
        while  i<len(g) and j<len(s):
            if s[j]>=g[i]: #the size of cookies >= greedy factor of child then we can satisfy the child and move to next child
                c+=1
                i+=1
                j+=1
            else:
                j+=1 #if cookie size is less than greedy factor of child then we move to next cookie and check if it can satisfy the child
        return c