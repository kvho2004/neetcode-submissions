class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0

        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        
        ans = count
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count -= 1
            if blocks[i] == 'W':
                count += 1
            ans = min(ans, count)

        return ans