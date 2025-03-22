class Solution:
    def reverse(self, x: int) -> int:
        ls = []
        temp = abs(x)
        for _ in range(len(str(temp))):
            ls.append(temp % 10)
            temp //= 10

        reversed_num = 0
        for i in ls:
            reversed_num = reversed_num * 10 + i

        if x < 0:
            reversed_num *= -1
            
        # Handle 32-bit integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            reversed_num = 0

        return reversed_num