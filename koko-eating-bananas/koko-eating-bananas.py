class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
            total = 0
            m = (l+r)//2
            for each in piles:
                total += math.ceil(each/m)
            if total > h:
                l = m + 1
            else:
                r = m 
        return r

