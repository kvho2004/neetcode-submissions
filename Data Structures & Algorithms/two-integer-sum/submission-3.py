class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,n in enumerate(nums):
            k = target - n
            if k in prev:
                return[prev[k], i]
            prev[n] = i
            
