class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        def solver(num):
            ans = 0
            while num:
                x = num%10
                ans += x**2
                num = num//10
            return ans
        while True:
            x = solver(num)
            if x == 1:
                return True
            if x in seen:
                return False
            seen.add(x)
            num = x
        return False