class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*(len(temperatures))
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i],i))
            elif stack[len(stack)-1][0] > temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while len(stack) and stack[len(stack)-1][0] < temperatures[i]:
                    x = stack[len(stack)-1]
                    ans[x[1]] = i - x[1]
                    stack.pop()
                stack.append((temperatures[i],i))
        return ans
