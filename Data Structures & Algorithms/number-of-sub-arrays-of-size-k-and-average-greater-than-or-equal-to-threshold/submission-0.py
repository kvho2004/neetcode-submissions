class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0

        ans = 0

        for R in range(k, len(arr) + 1):
            # print(arr[L:R])
            average = sum(arr[L:R])/k
            # print(average)
            if average >= threshold:
                ans += 1
            L += 1

        return ans

        