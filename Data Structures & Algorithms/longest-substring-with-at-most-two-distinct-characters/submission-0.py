class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = {}
        length = 0

        L, R = 0, 0

        while R < len(s):
            window[s[R]] = R
            R += 1

            if len(window) == 3:
                i = min(window.values())
                del window[s[i]]
                L = i + 1

            length = max(length, R - L)

        return length