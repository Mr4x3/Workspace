"""
1   2   3   4   5   6   7   8   9  10  11  12
2   4   6   8  10  12  14  16  18  20  22  24
3   6   9  12  15  18  21  24  27  30  33  36
"""
def Mux_Tbl(d):
    for i in range(1,d+1):
        for j in range(1,d+1):
            x=i*j
            print(' '*(4-len(str(x)))+str(x),end='')
        print('')
Mux_Tbl(12)

