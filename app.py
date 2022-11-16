import pandas as pd
import numpy as np

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

    return int(table[len(s1), len(s2)][:-1])



def get_suggestions(string, city_list):
    edit_list = {}
    for i in city_list:
        edit_list[i[0]] = calcDpTable(string.lower(), i[0].lower())

    sorted_edit_list = {k: v for k, v in sorted(edit_list.items(), key=lambda item: item[1])}

    return sorted_edit_list
        

if __name__ == "__main__":
    df = pd.read_csv('list_municipios.txt')
    print('===========================================')
    print('      Sugestão de nomes de cidades         ')
    print('===========================================')
    str_user = str(input('Insira o nome de uma cidade: '))
    print("\n")

    result = get_suggestions(str_user, df.values)
    min_ = 30
    for i, k in enumerate(result):
        if i < 4:
            print(f"{k}: {result[k]}")