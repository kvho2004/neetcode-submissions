class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        window = set()
        length = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[L])
                L += 1
            window.add(s[i])
            length = max(length, i - L + 1)

        return length
