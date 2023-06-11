class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        while l<=r:
            i = (l+r)//2
            t = i*(i+1)//2
            if t == n:
                return i
            elif t > n:
                r = i -1
            else:
                l = i +1
        return r
