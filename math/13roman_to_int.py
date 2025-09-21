class Solution:
    def romanToInt(self, s: str) -> int:
        s=s.upper()
        so_la_ma={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        tong=0
        for i in range(len(s)-1):
            if so_la_ma[s[i]]>=so_la_ma[s[i+1]]:
                tong+=so_la_ma[s[i]]
            else:
                tong-=so_la_ma[s[i]]
        tong+= so_la_ma[s[-1]]
        return tong
main = Solution()
print(main.romanToInt("MCMXCIV"))