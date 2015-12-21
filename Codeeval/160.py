import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    f=float(test)
    h=int(f)
    m=int(((f-h)*60))
    s=int((f-h-m/60)*3600)
    print('{0}.{1:02d}\'{2:02d}"'.format(h,m,s))
