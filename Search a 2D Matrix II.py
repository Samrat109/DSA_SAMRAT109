#Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    #Integers in each row are sorted in ascending from left to right.
    #Integers in each column are sorted in ascending from top to bottom.

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            else:
                row += 1

        return False