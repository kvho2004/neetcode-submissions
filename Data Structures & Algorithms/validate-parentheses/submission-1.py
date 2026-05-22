class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        d = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == d[s[i]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        