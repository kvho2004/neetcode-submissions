class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        unique = []
        for i in range(len(nums)):
            if nums[i] != val:
                unique.append(nums[i])
        nums[:len(unique)] = unique
        return len(unique)
        