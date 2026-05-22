class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my = {}

        for num in nums:
            if num not in my:
                my[num] = 0
            else:
                my[num] += 1
        
        arr = []
        for num, cnt in my.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        