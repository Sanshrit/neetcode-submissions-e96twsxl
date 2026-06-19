class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        seen = set(('+','-','*','/'))
        for x in tokens:
            if x not in seen:
                stack.append(int(x))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if x == '+':
                    stack.append(num1+num2)
                elif x == '*':
                    stack.append(num1*num2)
                elif x == '-':
                    stack.append(num2 - num1)
                else:
                    stack.append(int(num2/num1))
        return stack[0]
