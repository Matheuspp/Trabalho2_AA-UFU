import numpy as np
import time

def calcDpTable(s1, s2):
    ## Initialise the table with zeroes.
    table = np.zeros([len(s1)+1, len(s2)+1], dtype=np.dtype('U3'))

    # ### i - insertion
    # ### d - deletion
    # ### r - replacement

    # ### Fill in base cases
    for i in range(len(s1)+1):
        table[i,0] = str(i) + 'i'
    for j in range(len(s2)+1):
        table[0,j] = str(j) + 'd'

    ## Start filling the rest of the table with the help of formula
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:  ## do nothing.
                table[i, j] = table[i-1, j-1][:-1] + 'n'
            else:  ## min + 1.
                if min(int(table[i-1, j-1][:-1]), int(table[i-1, j][:-1]), int(table[i, j-1][:-1])) == int(table[i-1, j-1][:-1]):
                    table[i,j] = str(int(table[i-1, j-1][:-1]) + 1) + 'r'
                elif min(int(table[i-1, j-1][:-1]), int(table[i-1, j][:-1]), int(table[i, j-1][:-1])) == int(table[i, j-1][:-1]):
                    table[i,j] = str(int(table[i, j-1][:-1]) + 1) + 'd'
                elif min(int(table[i-1, j-1][:-1]), int(table[i-1, j][:-1]), int(table[i, j-1][:-1])) == int(table[i-1, j][:-1]):
                    table[i,j] = str(int(table[i-1, j][:-1]) + 1) + 'i'

    print('Total Edit Distance:', table[len(s1), len(s2)][:-1])

if __name__ == "__main__":
    s1 = "matheus"
    s2 = "matheus"
    tic = time.time()
    calcDpTable(s1, s2)
    toc = time.time()
    print(f'\nRuntime: {abs(toc-tic)}')
