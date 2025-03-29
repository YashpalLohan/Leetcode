class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y = int(date[0:4])
        m = int(date[5:7])
        d = int(date[8:])
        y1 = bin(y)
        m1 = bin(m)
        d1 = bin(d)
        y2 = (y1[2:])
        m2 = (m1[2:])
        d2 = (d1[2:])
        ans = y2 + "-" + m2 + "-" + d2
        return str(ans)