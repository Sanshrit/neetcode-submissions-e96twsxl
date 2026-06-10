class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            else:
                if stack:
                    t1 = stack[-1]
                    stack.pop()
                    if t1 == '[' and x!=']' or t1 == '(' and x!=')' or t1 == '{' and x!='}':
                        return False
                else:
                    return False
        if len(stack):
            return False
        return True