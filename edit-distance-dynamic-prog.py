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
    print(table)
    print('-----------------------------------')
    print('Distance:', table[len(s1), len(s2)][:-1])
    calcChangesList(s1, s2, table)

def calcChangesList(s1, s2, table):    
    i = len(s1)
    j = len(s2)
    changes = []  ## Initialising changes list
    flag = 0 ## This will tell when to break out of the loop
    changing_string = list(s2)  ## copying the string to reflect the changes as we go backtracing
    
    while i >= 0:
        if flag == 1:
            break
        while j >= 0:
            if table[i,j][-1] == 'n':  ## If there is an 'n' that means no changes needed simply move diagonally.
                j-=1
                i-=1
            elif table[i,j][-1] == 'r':  
                ## In case of a 'r' i.e. replace, we replace the character in the string, print appropriate statement and move diagonally.
                statement1 = str(s2[j-1]) + ' muda para ' + str(s1[i-1])
                changing_string[j-1] = s1[i-1]
                statement2 = 'Então, a string se torna: ' + ''.join(changing_string)
                changes.append([statement1,statement2])
                i-=1
                j-=1
            elif table[i,j][-1] == 'i':
                ## In case of a 'i' i.e. insertion, we insert the character in the string, print appropriate statement and move upwards.
                statement1 =  str(s1[i-1]) + ' na posição ' + str(j+1) 
                changing_string.insert(j, s1[i-1])
                statement2 = 'Então, a string se torna ' + ''.join(changing_string)
                changes.append([statement1,statement2])
                i-=1
            elif table[i,j][-1] == 'd':
                ## In case of a 'd' i.e. deletion, we delete the character in the string, print appropriate statement and move leftwards.
                statement1 = 'Remove ' + str(s2[j-1])
                del changing_string[j-1]
                statement2 = 'Então, a string se torna: ' + ''.join(changing_string)
                changes.append([statement1,statement2])
                j-=1
            if len(changes) == int(table[len(s1), len(s2)][:-1]):
                ## If total number of changes match the edit distance, we break out of the loop
                flag = 1
                break
    
    # Printing the list of changes
    print("\n\nTransformações:\n")
    for i in range(len(changes)):
        print(i+1,".", changes[i][0],'\n', changes[i][1], '\n')

if __name__ == "__main__":
    s1 = "natalia"
    s2 = "natali"
    print(s1+" -> "+ s2)
    print('-----------------------------------')
    tic = time.time()
    calcDpTable(s1, s2)
    toc = time.time()
    print(f'\nRuntime: {abs(toc-tic)}')
