class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
    # brute force
        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if j != i:
                    mult*=nums[j]
            pro.append(mult)
        return pro





