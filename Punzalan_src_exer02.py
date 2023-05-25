# Punzalan, Kurt Brian Daine B. Punzalan
# 2020-00772
# CMSC 180 - T-6L
# Exercise 01

import os 
import random
import time

os.system("cls")

#! FUNCTIONS
def printMatrix(M, n):
    for i in range(n):
        for j in range(n):
            print(M[i][j], end="\t")

        print()

def randomizeDivisible(M, n):
    # randomize values of all divisible by 10
    for row in range(n):
        for col in range(n):
            if (row % 10 == 0) and (col % 10 == 0):
                M[row][col] = float(random.randint(1,1000))

    return M

def terrain_inter_row(M, n, row):
    for index in range(n):
        if M[row][index] == 0:
            x = index # provide x based on the x-coordinate
            
            # apply the formula for FCC
            M[row][index] = round((y1 + ((x-x1)/(x2-x1)) * (y2-y1)), 2)
        else:
            # print(index, "index")
            x1 = index
            x2 = index + 10

            try:
                y1 = M[row][x1]
                y2 = M[row][x2]
            except:
                pass

    return M


def terrain_inter_col(M, n, col):
    for index in range(n):
        if M[index][col] == 0:
            x = index
            M[index][col] = round((y1 + ((x-x1)/(x2-x1)) * (y2-y1)), 2)

        else:
            x1 = index
            x2 = index + 10

            try:
                y1 = M[x1][col]
                y2 = M[x2][col]
            except:
                pass

    return M

#! MAIN

# user input
n = int(input("Input: ")) + 1

# matrix
M = [[0 for column in range(n)]for row in range(n)]
M = randomizeDivisible(M, n)

#! FCC
# calculate 
time_before = time.time()

# fill the rows whose columns are divisible by 10 
row = 0
while row < n:
    M = terrain_inter_row(M, n, row)
    row += 10


# fill the columns whose rows are divisible by 10 
col = 0
while col < n:
    M = terrain_inter_col(M, n, col)
    col += 10


# fill remaining rows (inner box)
for row in range(1, n-1):
    if row % 10 == 0:
        continue
    M = terrain_inter_row(M, n, row)

# for i in range(n):
#     for j in range(n):
#         print(f"({i}, {j})", end="\t")
#     print()

print()

printMatrix(M, n)

time_elapsed = time.time() - time_before

print("time elapsed:", time_elapsed)