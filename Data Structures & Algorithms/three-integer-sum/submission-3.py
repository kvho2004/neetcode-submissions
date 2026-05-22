class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                target = -nums[i]
                if nums[L] + nums[R] > target:
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

        return result
                    




        