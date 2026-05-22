class Solution:
    def trap(self, height: List[int]) -> int:
        maximum = 0
        L = 0
        while L < len(height) - 1:
            if height[L] == 0:
                L += 1
                continue
            
            best_R = -1
            # Find the first bar >= height[L] OR the highest bar after L
            for R in range(L + 1, len(height)):
                if height[R] >= height[L]:
                    best_R = R
                    break
                if best_R == -1 or height[R] >= height[best_R]:
                    best_R = R
            
            if best_R != -1:
                water_level = min(height[L], height[best_R])
                for i in range(L + 1, best_R):
                    maximum += max(0, water_level - height[i])
                L = best_R
            else:
                L += 1

        return maximum