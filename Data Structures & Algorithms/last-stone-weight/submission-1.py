import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-n for n in stones]
        heapq.heapify(h)


        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)

            # print(x, y)

            if x != y:
                heapq.heappush(h, -abs(y-x))
            
        if len(h) > 0:
            return -heapq.heappop(h)
        else:
            return 0
