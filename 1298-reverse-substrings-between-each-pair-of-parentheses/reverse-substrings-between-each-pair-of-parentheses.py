class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        result=[]
        for char in s:
            if char=='(':
                stack.append(result)
                result=[] 
            elif char==')':
                stack[-1].extend(reversed(result))
                result=stack.pop()
            else:
                result.append(char)
        return ''.join(result)