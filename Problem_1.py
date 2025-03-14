#This uses binary search and treats the array as a flatenned array 
# The divmod function is used to convert 1D indices into 2D row and column indices.
# Time Complexity = O(m*n)
#Space Complexity = O(1)

class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        if not matrix or not matrix[0]: 
            return False
    
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)  # Get row and column indices
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
            