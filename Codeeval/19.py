import sys
def bit_pos(x,y,z):
    k=bin(x)
    if k[y]==k[z]:
        return True
    
with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    x,y,z=test.split(',')
    x,y,z=int(x),-int(y),-int(z)
    if bit_pos(x,y,z):
        print('true')
    else:
        print('false')
