# Very Cool Code
import sys

matrix=[[0 for i in range(256)] for i in range(256)]


def SetRow(matrix,x):
    matrix[x[0]]=[x[1] for i in range(256)]

def SetCol(matrix,x):
    for i in matrix:
        i[x[0]]=x[1]

def QueryRow(matrix,x):
    print(sum(matrix[x[0]]))

def QueryCol(matrix,x):
    s=0
    for i in matrix:
        s=s+i[x[0]]
    print(s)


with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

dic={
    'SetCol':SetCol,'SetRow':SetRow,
    'QueryCol':QueryCol,'QueryRow':QueryRow
    }
for test in test_cases:
    z=[int(x) if x.isdigit() else x for x in test.split()]
    x=z[1:]
    r=z[0]
    dic.get(r)(matrix,x)
