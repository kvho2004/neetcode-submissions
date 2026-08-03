class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        threshold *= k
        average = sum(arr[:k - 1])
        for L in range(len(arr) - k + 1):
            average += arr[L + k - 1]
            if average >= threshold:
                ans += 1
            average -= arr[L]

        return ans

        