class Solution:
    def isPowerOf(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

print(Solution().isPowerOf(555))