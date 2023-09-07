#!/usr/bin/env python

# Importing the libraries
import numpy as np
import numpy.linalg as lg
# Importing the datasets
import csv

# =============================================================================
# ==> RETURN THE NAME OF THE QB WITH THE MAX NUMBER OF ATTEMPTS AND THE ATTEMPT
#     COUNT
# =============================================================================


def max_num_of_attempts():
    with open('data/Football_matrices_1998.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            data = list(csv.reader(csv_file))

    matrix1998 = np.matrix(data)
    # =============================================================================
    # Read in the matrix1999 file
    # =============================================================================
    with open('data/Football_matrices_1999.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            data = list(csv.reader(csv_file))

    matrix1999 = np.matrix(data)
    # =============================================================================
    # Strip off the names into a separate names list
    # =============================================================================
    names = matrix1998[:, 0]

    # =============================================================================
    # note that matrix1998 and matrix 1999 is a mixed type and the
    # numbers must be converted to floats - convert them to floats
    # =============================================================================
    matrix1998 = matrix1998[:, 1:].astype(float)
    matrix1999 = matrix1999[:, 1:].astype(float)
    print(matrix1998)
    print(matrix1999)

    # =============================================================================
    # Find the Difference and print
    # =============================================================================
    print(matrix1999 - matrix1998)

    # =============================================================================
    # print 2 year total
    # =============================================================================
    print(matrix1998 + matrix1999)

    # =============================================================================
    # print average of two years
    # =============================================================================
    print(np.mean(np.array([matrix1998, matrix1999]), axis=0))

    # =============================================================================
    # Who had and what was the amount of the max attempts for 1998
    # max values of each column (axis = 0) and print it out
    # ==> RETURN THE NAME OF THE QB WITH THE MAX NUMBER OF ATTEMPTS AND THE ATTEMPT
    #     COUNT
    # =============================================================================
    highest = np.max(matrix1998[:, 0], axis=0)
    idx = np.where(matrix1998[:, 0] == highest)
    print(f"{names[idx][0]} had {highest} attempts")

    return names[idx], highest


def dot_product():
    # =============================================================================
    #  Solve the dot product of the following
    #  From the Matrix packet Flower Arrangements
    #  Carl wants to buy flowers for two of his friends. Inga prefers mostly roses and
    #  Tasha prefers mostly lilies. Carl wants to buy two different arrangements.
    #  Inga’s arrangement will include 6 roses, 4 carnations, and 2 lilies.
    #  Tasha’s arrangement will include 3 roses, 3 carnations, and 6 lilies.
    #  As in question
    #  #1, Rose’s Flower Shop charges $2.25 for a rose, $1.25 for a carnation,
    #  and $1.95 for a lily. How much will each arrangement cost?
    #
    #  ==> RETURN THE ARRAY RESULTING FROM THE DOT PRODUCT
    # =============================================================================
    #AB = X
    A = np.array([[6, 4, 2],
                  [3, 3, 6]])
    B = np.array([2.25, 1.25, 1.95])
    
    return np.dot(A, B)


def solve_equation():
    # solve equation with linalg
    # Complete first example (soda, hot dogs and candy bar prices)
    # =============================================================================
    # System of equations:
    #  x + 2y +2z = 4.35 (Albert)
    # 2x + 3y + z = 4.40 (Megan)
    #  x +  3z = 4.50 (you)
    #
    # ==> RETURN THE SOLUTION MATRIX
    # =============================================================================
    #AX = B
    A = np.array([[1, 2, 2],
                  [2, 3, 1],
                  [1, 0, 3]])
    B = np.array([4.35, 4.40, 4.50])

    return np.dot(np.linalg.inv(A), B)


# =============================================================================
# Methods go above
# =============================================================================
qB, max_attempts = max_num_of_attempts()
print(qB, "had the maximum number of attempts in 1998 of",
      max_attempts)
print("dot product array: ", dot_product())
print("solution to equations: ", solve_equation())
