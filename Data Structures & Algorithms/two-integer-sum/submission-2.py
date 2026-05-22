class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                k = nums.index(target - nums[i])
                if (k != i):
                    return sorted([i, k])
            except ValueError:
                continue
            
