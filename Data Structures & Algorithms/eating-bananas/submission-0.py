class Solution:
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        while L < R:
            mid = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                R = mid
            else:
                L = mid + 1
        

        return R


