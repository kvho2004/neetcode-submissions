class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lit = []
        for i in range(len(nums)):
            try:
                k = nums.index(target - nums[i])
                if (k != i) and k not in lit:
                    lit.append(i)
                    lit.append(k)
            except ValueError:
                continue
        
        return sorted(lit)
            
