class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        # frequency of characters in the current window
        counts = collections.Counter()
        L = 0

        for R in range(len(s)):
            counts[s[R]] += 1
            # Window size - count of most frequent char = number of replacements needed
            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            
            maxLength = max(maxLength, R - L + 1)

        return maxLength