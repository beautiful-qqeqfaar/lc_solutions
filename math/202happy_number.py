class Solution:
    def isHappy(self, n: int) -> bool:
        da_qua = set()
        while n != 1 and n not in da_qua:
            da_qua.add(n)
            n = sum(int(i) ** 2 for i in str(n))

        return n == 1
print(Solution().isHappy(17))