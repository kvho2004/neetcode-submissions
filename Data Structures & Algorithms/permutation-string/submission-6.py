from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        L = 0
        comp = Counter(s1)
        n = len(s1)
        print(comp)
        for R in range(len(s1) - 1, len(s2)):
            sub = Counter(s2[L:R + 1])
            print(sub)
            if sub == comp:
                return True
            L += 1

        return False

            



        