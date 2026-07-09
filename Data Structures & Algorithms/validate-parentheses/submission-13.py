class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if stack:
                    if i == ')' and stack[-1]!='(':
                        return False
                    if i == ']' and stack[-1]!='[':
                        return False
                    if i == '}' and stack[-1]!='{':
                        return False
                else:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False