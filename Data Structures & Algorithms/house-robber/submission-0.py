class Solution:


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            else:
                cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
                return cache[i]

        return dfs(0)
            

            

            

        
# def dfs_recursive(graph, start_node, visited=None):
#     if visited is None:
#         visited = set()
    
#     visited.add(start_node)
#     print(start_node, end=" ")  # Process the current node

#     for neighbor in graph[start_node]:
#         if neighbor not in visited:
#             dfs_recursive(graph, neighbor, visited)

# Example usage:
# dfs_recursive(graph, 'A') # Output: A B D E F C
                



            

    # def dp(n):
    # if n < 2:
    #     return n

    # dp = [0, 1]
    # i = 2
    # while i <= n:
    #     tmp = dp[1]
    #     dp[1] = dp[0] + dp[1]
    #     dp[0] = tmp
    #     i += 1
    # return dp[1]
    # def memoization(n, cache):
    #     if n <= 1:
    #         return n
    #     if n in cache:
    #         return cache[n]

    #     cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    #     return cache[n]
        