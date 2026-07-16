class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 0
        for i in nums:
            # Found unique element
            if insertIndex < 2 or nums[insertIndex - 2] != i:
                # Updating insertIndex in our main array
                nums[insertIndex] = i
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex