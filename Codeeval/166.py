import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()
    '''
	hours = int(numberOfSeconds / 3600)
	minutes = int(numberOfSeconds / 60) % 60
	seconds = numberOfSeconds % 60
	'''


def time_diff(gap_sec):
    h=int(gap_sec/3600)
    m=int((gap_sec-h*3600)/60)
    s=int(gap_sec-h*3600-m*60)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
for test in test_cases:
    r,t=test.split()
    x1,y1,z1=[int(i) for i in r.split(':')]
    x2,y2,z2=[int(i) for i in t.split(':')]
    x1=x1*3600
    x2=x2*3600
    y1=y1*60
    y2=y2*60
    gap_sec=(x2+y2+z2)-(x1+y1+z1)
    print(time_diff(abs(gap_sec)))
