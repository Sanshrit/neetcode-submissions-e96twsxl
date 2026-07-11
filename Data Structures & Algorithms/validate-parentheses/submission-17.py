class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) ==0:
                return False
            elif i == ')' and stack[-1]!='(' or i == ']' and stack[-1]!='[' or i == '}' and stack[-1]!='{':
                return False
            else:
                stack.pop()
        if len(stack):
            return False
        return True
        