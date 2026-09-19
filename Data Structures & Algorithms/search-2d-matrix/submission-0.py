class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows ,Cols = len(matrix) ,len(matrix[0])
        top ,bot = 0 ,Rows - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l ,r = 0 ,Cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

obj = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
soln = obj.searchMatrix(matrix ,target)
print(soln)

# The matrix is sorted row-wise and the rows are also ordered.
# First, use binary search to find the row where the target could exist.
# Then, perform another binary search within that row to find the target.
# If the target is found, return True; otherwise, return False.
# Time: O(log(m) + log(n)), Space: O(1)