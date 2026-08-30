class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final = 0
        d = 1
        for i in range(1, len(digits)+1):
            final+=digits[-i]*d
            d = d * 10

        print(final)
        final = final + 1

        final = str(final)

        result = []
        for n in final:
            result.append(int(n))

        return result

        