class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for ch in s:
            if stack and stack[-1]==ch: #if top of stack is same as current character then pop the top of stack
                stack.pop()
            else:
                stack.append(ch) #if top of stack not equal to current character then append the character into stack
        return "".join(stack) #return the string formed by joining the characters in stack