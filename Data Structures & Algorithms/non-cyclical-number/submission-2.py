class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = 0
        while res != 1:
            res = 0
            print(n)
            while n > 0:
                digit = n % 10
                print(digit ** 2)
                res += digit ** 2
                n = (n - digit) // 10
                print(res)
                
            if res == 1:
                return True
            if res in seen:
                return False
            else:
                seen.add(res)
                n = res
            
            
        return True

        