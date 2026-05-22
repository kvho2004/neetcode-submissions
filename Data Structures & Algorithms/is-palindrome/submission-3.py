class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = ''.join(s for s in s if s.isalnum())
        s = s.lower()
        print(s)
        L = 0
        R = len(s) - 1

        while L < R:
            if s[L] != s[R]:
                print(s[L])
                print(s[R])
                return False
            L+=1
            R-=1
        return True