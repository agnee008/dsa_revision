"""
Create a DP table: Create a 2D DP table of the same dimensions as the input matrix.
Initialize DP table: Initialize the first row and first column of the DP table to be the same as the input matrix since the largest square ending at any cell in the first row or first column is the cell itself (if it is 1).
Fill the DP table: For each cell (i, j) in the matrix, if the cell contains a 1, update the DP table as follows:

This recurrence relation ensures that the value of dp[i][j] represents the side length of the largest square whose bottom-right corner is at (i, j).
Track the maximum side length: Keep track of the maximum side length found during the process.
Compute the area: The area of the largest square is the square of the maximum side length.

"""


def maximalSquare(matrix):
    if not matrix:
        return 0
    
    # Get dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the dp table with zeros
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0
    
    # Fill the dp table
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    # The area of the largest square
    return max_side * max_side

# Example usage:
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(maximalSquare(matrix))  # Output: 4
