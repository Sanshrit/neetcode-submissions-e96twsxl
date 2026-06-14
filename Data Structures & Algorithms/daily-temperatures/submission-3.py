class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([temperatures[i],i])
            elif stack[-1][0] > temperatures[i]:
                stack.append([temperatures[i],i])
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    temp,idx = stack.pop()
                    ans[idx] = i-idx
                stack.append([temperatures[i],i])
        return ans