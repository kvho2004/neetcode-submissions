import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        track = {}
        majority = [nums[0],0]
        for n in nums:
            if n not in track:
                track[n] = 1
            else:
                track[n] = track[n] + 1
                if track[n] > majority[1]:
                    majority[1] = track[n]
                    majority[0] = n

        return majority[0]

