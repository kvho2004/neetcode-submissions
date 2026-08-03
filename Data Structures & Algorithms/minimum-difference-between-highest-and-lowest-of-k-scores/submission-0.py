class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        sorted_arr = sorted(nums)

        ans = float('inf')

        for L in range(len(sorted_arr) - k + 1):
            diff = sorted_arr[L + k - 1] - sorted_arr[L]
            print(diff)
            ans = min(ans, diff)

        return ans