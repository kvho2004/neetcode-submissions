class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sorted so no hashmaps
        if len(nums) <= 1:
            return len(nums)
        
        unique = []
        unique.append(nums[0])
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique.append(nums[i])
                k = k + 1   
        for j in range(len(unique)):
            nums[j] = unique[j]
        return k
