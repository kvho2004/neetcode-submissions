class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        L, R = 0, len(nums) - 1

        if nums[0] < nums[R]:
            return nums[0]

        while L <= R:
            mid = L + (R - L) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                L = mid + 1
            else:
                R = mid - 1


