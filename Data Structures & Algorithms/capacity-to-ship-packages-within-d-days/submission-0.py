class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            total_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > mid:
                    total_days += 1
                    current_load = w
                else:
                    current_load += w
            if total_days <= days:
                r = mid
            else:
                l = mid + 1
        return l