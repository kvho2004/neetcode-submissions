class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = n - 1

        T = 0
        B = m - 1


        while (T <= B):
            midR = B - T // 2
            if target > matrix[midR][n - 1]:
                T = midR + 1
            elif target < matrix[midR][n - 1]:
                B = midR - 1
            else:
                return True
        
        Rt = max(T, B, midR)
        
        while (L <= R and Rt < m):
            midC = R - L // 2
            if target > matrix[Rt][midC]:
                L = midC + 1
            elif target < matrix[Rt][midC]:
                R = midC - 1
            else:
                return True

        
        return False