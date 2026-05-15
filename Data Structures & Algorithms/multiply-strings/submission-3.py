class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =="0" or num2 == "0":
            return  "0"
        st = deque()
        for ch in num1:
            n1 = ord(ch) - ord('0')
            st.append(n1)
        n1=0
        while st:
            curr = st.popleft()
            n1 = n1*10 + curr
        
        for ch in num2:
            n2 = ord(ch) - ord('0')
            st.append(n2)
        n2=0
        while st:
            curr = st.popleft()
            n2 = n2*10 + curr
        ans = n1*n2

        ans_s = deque()
        while ans:
            dig = ans%10
            ans_s.append(dig)
            ans = ans//10

        st = ""
        while ans_s:
            x = ans_s.popleft()
            st += str(x)
        return st[::-1]
