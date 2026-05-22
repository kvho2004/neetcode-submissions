class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        # montonically decreasing order sort(reverse = true)
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                temp, ind = stack.pop()
                result[ind] = i - ind
            stack.append((n,i))
        
        return result


                








            


