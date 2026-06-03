class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:   # target is in sorted left half
                    r = mid - 1
                else:                                # target is NOT in left half
                    l = mid + 1
            
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:   # target is in sorted right half
                    l = mid + 1
                else:                                # target is NOT in right half
                    r = mid - 1

        return -1

