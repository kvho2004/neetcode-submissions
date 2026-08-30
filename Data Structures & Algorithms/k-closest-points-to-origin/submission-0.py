class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        max_heap = []
        
        for x, y in points:
            # Calculate squared distance: x^2 + y^2 (avoids square root)
            sq_dist = x**2 + y**2
            
            # Store a tuple of (-sq_dist, x, y)
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (sq_dist, x, y))
            else:

                if sq_dist < max_heap[0][0]:
                    heapq.heappushpop_max(max_heap, (sq_dist, x, y))

        return [[x, y] for (_, x, y) in max_heap]