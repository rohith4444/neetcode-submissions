class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:       # this rate works, try smaller
                r = mid
            else:                # too slow, need bigger rate
                l = mid + 1
        return l