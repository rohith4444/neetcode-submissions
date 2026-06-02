class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = []
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    l = j - i + 1
                    length.append(l)
                    break

        if length:                    # ← this must be outside BOTH loops
            return min(length)
        else:
            return 0

#time complexity: O(n2) Space complexity: O(n)