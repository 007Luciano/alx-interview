#!/usr/bin/python3
""" rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of lists): The 2D matrix to rotate.
    Return:
        None
    """
    if not matrix:
        return

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
