class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}
        ans = []
        n = len(digits)
        def f(idx,s):
            if idx==n:
                ans.append(s)
                return
            dig = digits[idx]
            for ch in mapping[dig]:
                s+=ch
                f(idx+1,s)
                s = s[:-1]
        f(0,"")
        return ans

            