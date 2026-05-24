class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for x in tokens:
            if x not in {"+", "-", "*", "/"}:
                st.append(int(x))
            else:
                x1 = st.pop()
                x2 = st.pop()
                if x == '+':
                    st.append(x2+x1)
                elif x == '*':
                    st.append(x2*x1)
                elif x == '-':
                    st.append(x2-x1)
                else:
                    st.append(int(x2/x1))
        return st[0]
                
        
        