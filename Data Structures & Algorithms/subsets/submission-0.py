class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
    
        # For each number in the input array
        for num in nums:
            # Create new subsets by adding current number to all existing subsets
            new_subsets = []
            for subset in res:
                new_subset = subset + [num]
                new_subsets.append(new_subset)
            
            # Add all the new subsets to our result
            res = res + new_subsets
    
        return res


