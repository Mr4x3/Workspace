import sys

def reverse_sentance(sen):
    s=sen.split()
    sr=s[::-1]
    return sr

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    c=reverse_sentance(test)
    for i in c:
        print(i,end=' ')
    print('')
