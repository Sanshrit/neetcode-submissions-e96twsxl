class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        # sum = 0
        for i in range(len(digits)-1,-1,-1):
            # if i == len(digits)-1:
            #     sum = digits[i] + 1
            # else:
            #     sum = digits[i] + carry
            sum = digits[i] + carry
            digits[i] = sum%10
            carry = sum//10
            if carry == 0:
                return digits
        
        if carry:
            ans = [0 for _ in range(len(digits)+1)]
            ans[0] = carry
            for i in range(1,len(ans)):
                ans[i] = digits[i-1]
            return ans
        return digits
